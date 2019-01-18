/*
 * Copyright (c) 2018 Pilz GmbH & Co. KG
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef TRAJECTORY_FUNCTIONS_H
#define TRAJECTORY_FUNCTIONS_H

#include <Eigen/Geometry>
#include <kdl/trajectory.hpp>
#include <moveit/robot_model/robot_model.h>
#include <moveit/robot_state/robot_state.h>
#include <eigen_conversions/eigen_kdl.h>
#include <eigen_conversions/eigen_msg.h>
#include <trajectory_msgs/MultiDOFJointTrajectory.h>
#include <moveit/robot_trajectory/robot_trajectory.h>

#include "pilz_trajectory_generation/limits_container.h"
#include "pilz_trajectory_generation/cartesian_trajectory.h"


namespace pilz {

/**
 * @brief compute the inverse kinematics of a given pose, also check robot self collision
 * @param robot_model: kinematic model of the robot
 * @param group_name: name of planning group
 * @param link_name: name of target link
 * @param pose: target pose in IK solver Frame
 * @param frame_id: reference frame of the target pose
 * @param seed: seed state of IK solver
 * @param solution: solution of IK
 * @param check_self_collision: true to enable self collision checking after IK computation
 * @param max_attempt: maximal attempts of IK
 * @return true if succeed
 */
bool computePoseIK(const robot_model::RobotModelConstPtr& robot_model,
                   const std::string& group_name,
                   const std::string& link_name,
                   const Eigen::Affine3d& pose,
                   const std::string& frame_id,
                   const std::map<std::string, double>& seed,
                   std::map<std::string, double>& solution,
                   bool check_self_collision = true,
                   int max_attempt = 2);

bool computePoseIK(const robot_model::RobotModelConstPtr& robot_model,
                   const std::string& group_name,
                   const std::string& link_name,
                   const geometry_msgs::Pose& pose,
                   const std::string& frame_id,
                   const std::map<std::string, double>& seed,
                   std::map<std::string, double>& solution,
                   bool check_self_collision = true,
                   int max_attempt = 2);

/**
 * @brief compute the pose of a link at give robot state
 * @param robot_model: kinematic model of the robot
 * @param link_name: target link name
 * @param joint_state: joint positons of this group
 * @param pose: pose of the link in base frame of robot model
 * @return true if succeed
 */
bool computeLinkFK(const robot_model::RobotModelConstPtr& robot_model,
                   const std::string& link_name,
                   const std::map<std::string, double>& joint_state,
                   Eigen::Affine3d& pose);

bool computeLinkFK(const robot_model::RobotModelConstPtr& robot_model,
                   const std::string& link_name,
                   const std::vector<std::string>& joint_names,
                   const std::vector<double>& joint_positions,
                   Eigen::Affine3d& pose);

/**
 * @brief verify the velocity/acceleration limits of current sample (based on backward difference computation)
 * v(k) = [x(k) - x(k-1)]/[t(k) - t(k-1)]
 * a(k) = [v(k) - v(k-1)]/[t(k) - t(k-2)]*2
 * @param position_last: position of last sample
 * @param velocity_last: velocity of last sample
 * @param position_current: position of current sample
 * @param duration_last: duration of last sample
 * @param duration_current: duration of current sample
 * @param joint_limits: joint limits
 * @return
 */
bool verifySampleJointLimits(const std::map<std::string, double>& position_last,
                             const std::map<std::string, double>& velocity_last,
                             const std::map<std::string, double>& position_current,
                             double duration_last,
                             double duration_current,
                             const JointLimitsContainer &joint_limits);


/**
 * @brief Generate joint trajectory from a KDL Cartesian trajectory
 * @param robot_model: robot kinematics model
 * @param joint_limits: joint limits
 * @param trajectory: KDL Cartesian trajectory
 * @param group_name: name of the planning group
 * @param link_name: name of the target robot link
 * @param initial_joint_position: initial joint positions, needed for selecting the ik solution
 * @param sampling_time: sampling time of the generated trajectory
 * @param joint_trajectory: output as robot joint trajectory, first and last point will have zero velocity
 * and acceleration
 * @param error_code: detailed error information
 * @param check_self_collision: check for self collision during creation
 * @return true if succeed
 */
bool generateJointTrajectory(const robot_model::RobotModelConstPtr& robot_model,
                             const JointLimitsContainer& joint_limits,
                             const KDL::Trajectory& trajectory,
                             const std::string& group_name,
                             const std::string& link_name,
                             const std::map<std::string, double>& initial_joint_position,
                             const double& sampling_time,
                             trajectory_msgs::JointTrajectory& joint_trajectory,
                             moveit_msgs::MoveItErrorCodes& error_code,
                             bool check_self_collision = false);

/**
 * @brief Generate joint trajectory from a MultiDOFJointTrajectory
 * @param trajectory: Cartesian trajectory
 * @param info: motion plan information
 * @param sampling_time
 * @param joint_trajectory
 * @param error_code
 * @return true if succeed
 */
bool generateJointTrajectory(const robot_model::RobotModelConstPtr& robot_model,
                             const JointLimitsContainer& joint_limits,
                             const pilz::CartesianTrajectory& trajectory,
                             const std::string& group_name,
                             const std::string& link_name,
                             const std::map<std::string, double>& initial_joint_position,
                             const std::map<std::string, double>& initial_joint_velocity,
                             trajectory_msgs::JointTrajectory& joint_trajectory,
                             moveit_msgs::MoveItErrorCodes& error_code,
                             bool check_self_collision = false);


/**
 * @brief Determines the sampling time and checks that both trajectroies use the
 * same sampling time.
 * @return TRUE if the sampling time is equal between all given points (except the last two points
 * of each trajectory), otherwise FALSE.
 */
bool determineAndCheckSamplingTime(const robot_trajectory::RobotTrajectoryPtr& first_trajectory,
                                   const robot_trajectory::RobotTrajectoryPtr& second_trajectory,
                                   double EPSILON,
                                   double& sampling_time);

/**
 * @brief Deprecated, do not use this function signature anymore.
 *
 * @deprecated use the other function signature taking const references to the robot states.
 *
 */
bool isRobotStateEqual(const robot_state::RobotStatePtr& state1,
                       const robot_state::RobotStatePtr& state2,
                       const std::string& joint_group_name,
                       double epsilon);

/**
 * @brief Check if the two robot states have the same joint position/velocity/acceleration.
 *
 * @param joint_group_name The name of the joint group.
 * @param epsilon Constants defining how close the joint position/velocity/acceleration have to be to be
 * recognized as equal.
 *
 * @return True if joint positions, joint velocities and joint accelerations are equal, otherwise false.
 */
bool isRobotStateEqual(const robot_state::RobotState& state1,
                       const robot_state::RobotState& state2,
                       const std::string& joint_group_name,
                       double epsilon);

/**
 * @brief check if the robot state have zero velocity/acceleartion
 * @param state
 * @param group
 * @param EPSILON
 * @return
 */
bool isRobotStateStationary(const robot_state::RobotStatePtr& state,
                            const std::string& group,
                            double EPSILON);


/**
 * @brief Performs a linear search for the intersection point of the trajectory with the blending radius.
 * @param center_position Center of blending sphere.
 * @param r Radius of blending sphere.
 * @param traj The trajectory.
 * @param inverseOrder TRUE: Farthest element from blending sphere center is located at the
 * smallest index of trajectroy.
 * @param index The intersection index which has to be determined.
 */
bool linearSearchIntersectionPoint(const std::string &link_name,
                                   const Eigen::Vector3d &center_position,
                                   const double &r,
                                   const robot_trajectory::RobotTrajectoryPtr& traj,
                                   bool inverseOrder,
                                   std::size_t &index);


bool intersectionFound(const Eigen::Vector3d &p_center,
                       const Eigen::Vector3d &p_current,
                       const Eigen::Vector3d &p_next,
                       const double& r);
}

#endif // TRAJECTORY_FUNCTIONS_H
