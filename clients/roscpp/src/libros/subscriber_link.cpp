/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
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

#include "ros/subscriber_link.h"
#include "ros/publication.h"

#include <boost/bind.hpp>

namespace ros
{

SubscriberLink::SubscriberLink()
  : connection_id_(0)
{

}

SubscriberLink::~SubscriberLink()
{

}

bool SubscriberLink::verifyDatatype(const std::string &datatype)
{
  PublicationPtr parent = parent_.lock();
  if (!parent)
  {
    ROS_ERROR("Trying to verify the datatype on a publisher without a parent");
    ROS_BREAK();

    return false;
  }

  if (datatype != parent->getDataType())
  {
    ROS_ERROR( "tried to send a message with type %s on a " \
                       "TransportSubscriberLink that has datatype %s",
                datatype.c_str(), parent->getDataType().c_str());
    return false; // todo: figure out a way to log this error
  }

  return true;
}

const std::string& SubscriberLink::getMD5Sum()
{
  PublicationPtr parent = parent_.lock();
  return parent->getMD5Sum();
}

const std::string& SubscriberLink::getDataType()
{
  PublicationPtr parent = parent_.lock();
  return parent->getDataType();
}

const std::string& SubscriberLink::getMessageDefinition()
{
  PublicationPtr parent = parent_.lock();
  return parent->getMessageDefinition();
}

} // namespace ros
