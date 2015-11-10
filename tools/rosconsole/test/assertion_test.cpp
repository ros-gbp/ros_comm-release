/*
 * Copyright (c) 2008, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#define ROS_ASSERT_ENABLED

#include "ros/assert.h"

#include <gtest/gtest.h>

void doAssert()
{
  ROS_ASSERT(false);
}

void doBreak()
{
  ROS_BREAK();
}

void doAssertMessage()
{
  ROS_ASSERT_MSG(false, "Testing %d %d %d", 1, 2, 3);
}

TEST(RosAssert, assert)
{
  ROS_ASSERT(true);

  EXPECT_DEATH(doAssert(), "ASSERTION FAILED");
}

TEST(RosAssert, breakpoint)
{
  EXPECT_DEATH(doBreak(), "BREAKPOINT HIT");
}

TEST(RosAssert, assertWithMessage)
{
  ROS_ASSERT_MSG(true, "Testing %d %d %d", 1, 2, 3);
  EXPECT_DEATH(doAssertMessage(), "Testing 1 2 3");
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  ros::Time::init();
  testing::FLAGS_gtest_death_test_style = "threadsafe";

  return RUN_ALL_TESTS();
}
