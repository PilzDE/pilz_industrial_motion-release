/*
 * Copyright (c) 2019 Pilz GmbH & Co. KG
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef CIRC_AUXILIARY_TYPES_H
#define CIRC_AUXILIARY_TYPES_H

#include "center.h"
#include "interim.h"
#include "cartesianconfiguration.h"
#include "cartesianpathconstraintsbuilder.h"

namespace pilz_industrial_motion_testutils
{

using CartesianCenter = Center<CartesianConfiguration, CartesianPathConstraintsBuilder>;
using CartesianInterim = Interim<CartesianConfiguration, CartesianPathConstraintsBuilder>;

}

#endif // CIRC_AUXILIARY_TYPES_H
