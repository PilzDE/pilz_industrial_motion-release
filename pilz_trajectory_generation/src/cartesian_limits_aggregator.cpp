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

#include "ros/ros.h"

#include "pilz_trajectory_generation/cartesian_limits_aggregator.h"

static const std::string param_cartesian_limits_ns = "cartesian_limits";

static const std::string param_max_trans_vel = "max_trans_vel";
static const std::string param_max_trans_acc = "max_trans_acc";
static const std::string param_max_trans_dec = "max_trans_dec";
static const std::string param_max_rot_vel = "max_rot_vel";
static const std::string param_max_rot_acc = "max_rot_acc";
static const std::string param_max_rot_dec = "max_rot_dec";

pilz::CartesianLimit pilz::CartesianLimitsAggregator::getAggregatedLimits(const ros::NodeHandle& nh)
{

  std::string param_prefix = param_cartesian_limits_ns + "/";

  pilz::CartesianLimit cartesian_limit;

  // translational velocity
  double max_trans_vel;
  if(nh.getParam(param_prefix + param_max_trans_vel, max_trans_vel))
  {
    cartesian_limit.setMaxTranslationalVelocity(max_trans_vel);
  }

  // translational acceleration
  double max_trans_acc;
  if(nh.getParam(param_prefix + param_max_trans_acc, max_trans_acc))
  {
    cartesian_limit.setMaxTranslationalAcceleration(max_trans_acc);
  }

  // translational deceleration
  double max_trans_dec;
  if(nh.getParam(param_prefix + param_max_trans_dec, max_trans_dec))
  {
    cartesian_limit.setMaxTranslationalDeceleration(max_trans_dec);
  }

  // rotational velocity
  double max_rot_vel;
  if(nh.getParam(param_prefix + param_max_rot_vel, max_rot_vel))
  {
    cartesian_limit.setMaxRotationalVelocity(max_rot_vel);
  }

  // rotational acceleration + deceleration deprecated
  // LCOV_EXCL_START
  if(nh.hasParam(param_prefix + param_max_rot_acc)
     || nh.hasParam(param_prefix + param_max_rot_dec))
  {
    ROS_WARN_STREAM("Ignoring cartesian limits parameters for rotational acceleration / deceleration;"
                    << "these parameters are deprecated and are automatically calculated from"
                    << "translational to rotational ratio.");
  }
  // LCOV_EXCL_STOP

  return cartesian_limit;

}
