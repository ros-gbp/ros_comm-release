# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import unittest
import time

# mock of subscription tests
class ThreadPoolMock(object):
    def queue_task(*args): pass

class TestRosmasterRegistrations(unittest.TestCase):

    def test_NodeRef_services(self):
        from rosmaster.registrations import NodeRef, Registrations
        n = NodeRef('n1', 'http://localhost:1234')
        # test services
        n.add(Registrations.SERVICE, 'add_two_ints')
        self.assertFalse(n.is_empty())
        self.assertTrue('add_two_ints' in n.services)
        self.assertEqual(['add_two_ints'], n.services)
        
        n.add(Registrations.SERVICE, 'add_three_ints')
        self.assertFalse(n.is_empty())
        self.assertTrue('add_three_ints' in n.services)
        self.assertTrue('add_two_ints' in n.services)

        n.remove(Registrations.SERVICE, 'add_two_ints')
        self.assertTrue('add_three_ints' in n.services)
        self.assertEqual(['add_three_ints'], n.services)
        self.assertFalse('add_two_ints' in n.services)
        self.assertFalse(n.is_empty())
        
        n.remove(Registrations.SERVICE, 'add_three_ints')        
        self.assertFalse('add_three_ints' in n.services)
        self.assertFalse('add_two_ints' in n.services)
        self.assertEqual([], n.services)
        self.assertTrue(n.is_empty())

    def test_NodeRef_subs(self):
        from rosmaster.registrations import NodeRef, Registrations
        n = NodeRef('n1', 'http://localhost:1234')
        # test topic suscriptions
        n.add(Registrations.TOPIC_SUBSCRIPTIONS, 'topic1')
        self.assertFalse(n.is_empty())
        self.assertTrue('topic1' in n.topic_subscriptions)
        self.assertEqual(['topic1'], n.topic_subscriptions)
        
        n.add(Registrations.TOPIC_SUBSCRIPTIONS, 'topic2')
        self.assertFalse(n.is_empty())
        self.assertTrue('topic2' in n.topic_subscriptions)
        self.assertTrue('topic1' in n.topic_subscriptions)

        n.remove(Registrations.TOPIC_SUBSCRIPTIONS, 'topic1')
        self.assertTrue('topic2' in n.topic_subscriptions)
        self.assertEqual(['topic2'], n.topic_subscriptions)
        self.assertFalse('topic1' in n.topic_subscriptions)
        self.assertFalse(n.is_empty())
        
        n.remove(Registrations.TOPIC_SUBSCRIPTIONS, 'topic2')        
        self.assertFalse('topic2' in n.topic_subscriptions)
        self.assertFalse('topic1' in n.topic_subscriptions)
        self.assertEqual([], n.topic_subscriptions)
        self.assertTrue(n.is_empty())

    def test_NodeRef_pubs(self):
        from rosmaster.registrations import NodeRef, Registrations
        n = NodeRef('n1', 'http://localhost:1234')
        # test topic publications
        n.add(Registrations.TOPIC_PUBLICATIONS, 'topic1')
        self.assertFalse(n.is_empty())
        self.assertTrue('topic1' in n.topic_publications)
        self.assertEqual(['topic1'], n.topic_publications)
        
        n.add(Registrations.TOPIC_PUBLICATIONS, 'topic2')
        self.assertFalse(n.is_empty())
        self.assertTrue('topic2' in n.topic_publications)
        self.assertTrue('topic1' in n.topic_publications)

        n.remove(Registrations.TOPIC_PUBLICATIONS, 'topic1')
        self.assertTrue('topic2' in n.topic_publications)
        self.assertEqual(['topic2'], n.topic_publications)
        self.assertFalse('topic1' in n.topic_publications)
        self.assertFalse(n.is_empty())
        
        n.remove(Registrations.TOPIC_PUBLICATIONS, 'topic2')        
        self.assertFalse('topic2' in n.topic_publications)
        self.assertFalse('topic1' in n.topic_publications)
        self.assertEqual([], n.topic_publications)
        self.assertTrue(n.is_empty())

    def test_NodeRef_base(self):
        import rosmaster.exceptions
        from rosmaster.registrations import NodeRef, Registrations
        n = NodeRef('n1', 'http://localhost:1234')
        self.assertEqual('http://localhost:1234', n.api)
        self.assertEqual([], n.param_subscriptions)
        self.assertEqual([], n.topic_subscriptions)
        self.assertEqual([], n.topic_publications)
        self.assertEqual([], n.services)
        self.assertTrue(n.is_empty())

        try:
            n.add(12345, 'topic')
            self.fail("should have failed with invalid type")
        except rosmaster.exceptions.InternalException: pass
        try:
            n.remove(12345, 'topic')
            self.fail("should have failed with invalid type")
        except rosmaster.exceptions.InternalException: pass

        n.add(Registrations.TOPIC_PUBLICATIONS, 'topic1')
        n.add(Registrations.TOPIC_PUBLICATIONS, 'topic2')
        n.add(Registrations.TOPIC_SUBSCRIPTIONS, 'topic2')        
        n.add(Registrations.TOPIC_SUBSCRIPTIONS, 'topic3')        
        n.add(Registrations.PARAM_SUBSCRIPTIONS, 'topic4')        
        n.add(Registrations.SERVICE, 'serv')        
        self.assertFalse(n.is_empty())

        n.clear()
        self.assertTrue(n.is_empty())        

    def test_NodeRef_param_subs(self):
        from rosmaster.registrations import NodeRef, Registrations
        n = NodeRef('n1', 'http://localhost:1234')
        # test param suscriptions
        n.add(Registrations.PARAM_SUBSCRIPTIONS, 'param1')
        self.assertFalse(n.is_empty())
        self.assertTrue('param1' in n.param_subscriptions)
        self.assertEqual(['param1'], n.param_subscriptions)
        
        n.add(Registrations.PARAM_SUBSCRIPTIONS, 'param2')
        self.assertFalse(n.is_empty())
        self.assertTrue('param2' in n.param_subscriptions)
        self.assertTrue('param1' in n.param_subscriptions)

        n.remove(Registrations.PARAM_SUBSCRIPTIONS, 'param1')
        self.assertTrue('param2' in n.param_subscriptions)
        self.assertEqual(['param2'], n.param_subscriptions)
        self.assertFalse('param1' in n.param_subscriptions)
        self.assertFalse(n.is_empty())
        
        n.remove(Registrations.PARAM_SUBSCRIPTIONS, 'param2')        
        self.assertFalse('param2' in n.param_subscriptions)
        self.assertFalse('param1' in n.param_subscriptions)
        self.assertEqual([], n.param_subscriptions)
        self.assertTrue(n.is_empty())

    ## subroutine of registration tests that test topic/param type Reg objects
    ## @param r Registrations: initialized registrations object to test
    def _subtest_Registrations_basic(self, r):
        #NOTE: no real difference between topic and param names, so tests are reusable

        # - note that we've updated node1's API
        r.register('topic1', 'node1', 'http://node1:5678')
        self.assertTrue('topic1' in r) # test contains
        self.assertTrue(r.has_key('topic1')) # test contains
        self.assertEqual(['topic1'], [k for k in r.iterkeys()])
        self.assertEqual(['http://node1:5678'], r.get_apis('topic1'))
        self.assertEqual([('node1', 'http://node1:5678')], r['topic1'])
        self.assertFalse(not r) #test nonzero
        self.assertEqual(None, r.get_service_api('topic1')) #make sure no contamination
        self.assertEqual([['topic1', ['node1']]], r.get_state())

        r.register('topic1', 'node2', 'http://node2:5678')
        self.assertEqual(['topic1'], [k for k in r.iterkeys()])        
        self.assertEqual(['topic1'], [k for k in r.iterkeys()])
        self.assertEqual(2, len(r.get_apis('topic1')))
        self.assertTrue('http://node1:5678' in r.get_apis('topic1'))
        self.assertTrue('http://node2:5678' in r.get_apis('topic1'))
        self.assertEqual(2, len(r['topic1']))
        self.assertTrue(('node1', 'http://node1:5678') in r['topic1'], r['topic1'])
        self.assertTrue(('node2', 'http://node2:5678') in r['topic1'])                
        self.assertEqual([['topic1', ['node1', 'node2']]], r.get_state())

        # TODO: register second topic
        r.register('topic2', 'node3', 'http://node3:5678')
        self.assertTrue('topic2' in r) # test contains
        self.assertTrue(r.has_key('topic2')) # test contains
        self.assertTrue('topic1' in [k for k in r.iterkeys()])
        self.assertTrue('topic2' in [k for k in r.iterkeys()])
        self.assertEqual(['http://node3:5678'], r.get_apis('topic2'))
        self.assertEqual([('node3', 'http://node3:5678')], r['topic2'])
        self.assertFalse(not r) #test nonzero
        self.assertTrue(['topic1', ['node1', 'node2']] in r.get_state(), r.get_state())
        self.assertTrue(['topic2', ['node3']] in r.get_state(), r.get_state())
        
        # Unregister

        # - fail if node is not registered
        code, _, val = r.unregister('topic1', 'node3', 'http://node3:5678')
        self.assertEqual(0, val)
        # - fail if topic is not registered by that node
        code, _, val = r.unregister('topic2', 'node2', 'http://node2:5678')
        self.assertEqual(0, val)
        # - fail if URI does not match
        code, _, val = r.unregister('topic2', 'node2', 'http://fakenode2:5678')
        self.assertEqual(0, val)

        # - unregister node2
        code, _, val = r.unregister('topic1', 'node1', 'http://node1:5678')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertTrue('topic1' in r) # test contains
        self.assertTrue(r.has_key('topic1')) 
        self.assertTrue('topic1' in [k for k in r.iterkeys()])
        self.assertTrue('topic2' in [k for k in r.iterkeys()])
        self.assertEqual(['http://node2:5678'], r.get_apis('topic1'))
        self.assertEqual([('node2', 'http://node2:5678')], r['topic1'])
        self.assertFalse(not r) #test nonzero
        self.assertTrue(['topic1', ['node2']] in r.get_state())
        self.assertTrue(['topic2', ['node3']] in r.get_state())        

        code, _, val = r.unregister('topic1', 'node2', 'http://node2:5678')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertFalse('topic1' in r) # test contains
        self.assertFalse(r.has_key('topic1')) 
        self.assertEqual(['topic2'], [k for k in r.iterkeys()])
        self.assertEqual([], r.get_apis('topic1'))
        self.assertEqual([], r['topic1'])
        self.assertFalse(not r) #test nonzero
        self.assertEqual([['topic2', ['node3']]], r.get_state())

        # clear out last reg
        code, _, val = r.unregister('topic2', 'node3', 'http://node3:5678')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertFalse('topic2' in r) # test contains
        self.assertTrue(not r)
        self.assertEqual([], r.get_state())        
        
    def test_Registrations(self):
        import rosmaster.exceptions
        from rosmaster.registrations import Registrations
        types = [Registrations.TOPIC_SUBSCRIPTIONS,
                 Registrations.TOPIC_PUBLICATIONS,
                 Registrations.SERVICE,
                 Registrations.PARAM_SUBSCRIPTIONS]
        # test enums
        self.assertEqual(4, len(set(types)))
        try:
            r = Registrations(-1)
            self.fail("Registrations accepted invalid type")
        except rosmaster.exceptions.InternalException: pass
        
        for t in types:
            r = Registrations(t)
            self.assertEqual(t, r.type)
            self.assertTrue(not r) #test nonzero
            self.assertFalse('topic1' in r) #test contains            
            self.assertFalse(r.has_key('topic1')) #test has_key
            self.assertFalse([k for k in r.iterkeys()]) #no keys
            self.assertEqual(None, r.get_service_api('non-existent'))

        # Test topic subs
        r = Registrations(Registrations.TOPIC_SUBSCRIPTIONS)
        self._subtest_Registrations_basic(r)
        r = Registrations(Registrations.TOPIC_PUBLICATIONS)        
        self._subtest_Registrations_basic(r)
        r = Registrations(Registrations.PARAM_SUBSCRIPTIONS)        
        self._subtest_Registrations_basic(r)

        r = Registrations(Registrations.SERVICE)        
        self._subtest_Registrations_services(r)

    def test_RegistrationManager_services(self):
        from rosmaster.registrations import Registrations, RegistrationManager
        rm = RegistrationManager(ThreadPoolMock())
        
        self.assertEqual(None, rm.get_node('caller1'))

        # do an unregister first, before service_api is initialized
        code, msg, val = rm.unregister_service('s1', 'caller1', 'rosrpc://one:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        
        rm.register_service('s1', 'caller1', 'http://one:1234', 'rosrpc://one:1234')
        self.assertTrue(rm.services.has_key('s1'))
        self.assertEqual('rosrpc://one:1234', rm.services.get_service_api('s1')) 
        self.assertEqual('http://one:1234', rm.get_node('caller1').api)
        self.assertEqual([['s1', ['caller1']]], rm.services.get_state())
        
        # - verify that changed caller_api updates ref
        rm.register_service('s1', 'caller1', 'http://oneB:1234', 'rosrpc://one:1234')
        self.assertTrue(rm.services.has_key('s1'))
        self.assertEqual('rosrpc://one:1234', rm.services.get_service_api('s1'))        
        self.assertEqual('http://oneB:1234', rm.get_node('caller1').api)
        self.assertEqual([['s1', ['caller1']]], rm.services.get_state())
        
        # - verify that changed service_api updates ref
        rm.register_service('s1', 'caller1', 'http://oneB:1234', 'rosrpc://oneB:1234')
        self.assertTrue(rm.services.has_key('s1'))
        self.assertEqual('rosrpc://oneB:1234', rm.services.get_service_api('s1'))        
        self.assertEqual('http://oneB:1234', rm.get_node('caller1').api)
        self.assertEqual([['s1', ['caller1']]], rm.services.get_state())
        
        rm.register_service('s2', 'caller2', 'http://two:1234', 'rosrpc://two:1234')
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)

        # - unregister should be noop if service api does not match
        code, msg, val = rm.unregister_service('s2', 'caller2', 'rosrpc://b:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        self.assertTrue(rm.services.has_key('s2'))
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)        
        self.assertEqual('rosrpc://two:1234', rm.services.get_service_api('s2'))
        
        # - unregister should be noop if service is unknown
        code, msg, val = rm.unregister_service('unknown', 'caller2', 'rosrpc://two:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        self.assertTrue(rm.services.has_key('s2'))
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)        
        self.assertEqual('rosrpc://two:1234', rm.services.get_service_api('s2'))

        # - unregister should clear all knowledge of caller2
        code,msg, val = rm.unregister_service('s2', 'caller2', 'rosrpc://two:1234')
        self.assertEqual(1, code)
        self.assertEqual(1, val)        
        self.assertTrue(rm.services.has_key('s1')) 
        self.assertFalse(rm.services.has_key('s2'))        
        self.assertEqual(None, rm.get_node('caller2'))

        code, msg, val = rm.unregister_service('s1', 'caller1', 'rosrpc://oneB:1234')
        self.assertEqual(1, code)        
        self.assertEqual(1, val)        
        self.assertTrue(not rm.services.__nonzero__())
        self.assertFalse(rm.services.has_key('s1'))        
        self.assertEqual(None, rm.get_node('caller1'))        

    def test_RegistrationManager_topic_pub(self):
        from rosmaster.registrations import Registrations, RegistrationManager
        rm = RegistrationManager(ThreadPoolMock())
        self.subtest_RegistrationManager(rm, rm.publishers, rm.register_publisher, rm.unregister_publisher)
        
    def test_RegistrationManager_topic_sub(self):
        from rosmaster.registrations import Registrations, RegistrationManager
        rm = RegistrationManager(ThreadPoolMock())
        self.subtest_RegistrationManager(rm, rm.subscribers, rm.register_subscriber, rm.unregister_subscriber)
    def test_RegistrationManager_param_sub(self):
        from rosmaster.registrations import Registrations, RegistrationManager
        rm = RegistrationManager(ThreadPoolMock())
        self.subtest_RegistrationManager(rm, rm.param_subscribers, rm.register_param_subscriber, rm.unregister_param_subscriber)
        
    def subtest_RegistrationManager(self, rm, r, register, unregister):
        self.assertEqual(None, rm.get_node('caller1'))

        register('key1', 'caller1', 'http://one:1234')
        self.assertTrue(r.has_key('key1'))
        self.assertEqual('http://one:1234', rm.get_node('caller1').api)
        self.assertEqual([['key1', ['caller1']]], r.get_state())
        
        # - verify that changed caller_api updates ref
        register('key1', 'caller1', 'http://oneB:1234')
        self.assertTrue(r.has_key('key1'))
        self.assertEqual('http://oneB:1234', rm.get_node('caller1').api)
        self.assertEqual([['key1', ['caller1']]], r.get_state())
        
        register('key2', 'caller2', 'http://two:1234')
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)

        # - unregister should be noop if caller api does not match
        code, msg, val = unregister('key2', 'caller2', 'http://b:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)        
        
        # - unregister should be noop if key is unknown
        code, msg, val = unregister('unknown', 'caller2', 'http://two:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        self.assertTrue(r.has_key('key2'))
        self.assertEqual('http://two:1234', rm.get_node('caller2').api)        

        # - unregister should be noop if unknown node
        code, msg, val = rm.unregister_publisher('key2', 'unknown', 'http://unknown:1')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        
        self.assertTrue(r.has_key('key2'))

        # - unregister should clear all knowledge of caller2
        code,msg, val = unregister('key2', 'caller2', 'http://two:1234')
        self.assertEqual(1, code)
        self.assertEqual(1, val)        
        self.assertTrue(r.has_key('key1')) 
        self.assertFalse(r.has_key('key2'))        
        self.assertEqual(None, rm.get_node('caller2'))

        code, msg, val = unregister('key1', 'caller1', 'http://oneB:1234')
        self.assertEqual(1, code)        
        self.assertEqual(1, val)        
        self.assertTrue(not r.__nonzero__())
        self.assertFalse(r.has_key('key1'))        
        self.assertEqual(None, rm.get_node('caller1'))        

    def test_RegistrationManager_base(self):
        import rosmaster.exceptions
        from rosmaster.registrations import Registrations, RegistrationManager
        threadpool = ThreadPoolMock()

        rm = RegistrationManager(threadpool)
        self.assertTrue(isinstance(rm.services, Registrations))
        self.assertEqual(Registrations.SERVICE, rm.services.type)
        self.assertTrue(isinstance(rm.param_subscribers, Registrations))
        self.assertEqual(Registrations.PARAM_SUBSCRIPTIONS, rm.param_subscribers.type)
        self.assertTrue(isinstance(rm.subscribers, Registrations))
        self.assertEqual(Registrations.TOPIC_SUBSCRIPTIONS, rm.subscribers.type)
        self.assertTrue(isinstance(rm.subscribers, Registrations))
        self.assertEqual(Registrations.TOPIC_PUBLICATIONS, rm.publishers.type)
        self.assertTrue(isinstance(rm.publishers, Registrations))

        #test auto-clearing of registrations if node API changes
        rm.register_publisher('pub1', 'caller1', 'http://one:1')
        rm.register_publisher('pub1', 'caller2', 'http://two:1')
        rm.register_publisher('pub1', 'caller3', 'http://three:1')
        rm.register_subscriber('sub1', 'caller1', 'http://one:1')
        rm.register_subscriber('sub1', 'caller2', 'http://two:1')
        rm.register_subscriber('sub1', 'caller3', 'http://three:1')
        rm.register_param_subscriber('p1', 'caller1', 'http://one:1')
        rm.register_param_subscriber('p1', 'caller2', 'http://two:1')
        rm.register_param_subscriber('p1', 'caller3', 'http://three:1')
        rm.register_service('s1', 'caller1', 'http://one:1', 'rosrpc://one:1')
        self.assertEqual('http://one:1', rm.get_node('caller1').api)
        self.assertEqual('http://two:1', rm.get_node('caller2').api)
        self.assertEqual('http://three:1', rm.get_node('caller3').api)        

        # - first, make sure that changing rosrpc URI does not erase state
        rm.register_service('s1', 'caller1', 'http://one:1', 'rosrpc://oneB:1')
        n = rm.get_node('caller1')
        self.assertEqual(['pub1'], n.topic_publications)
        self.assertEqual(['sub1'], n.topic_subscriptions)
        self.assertEqual(['p1'], n.param_subscriptions)                
        self.assertEqual(['s1'], n.services)
        self.assertTrue('http://one:1' in rm.publishers.get_apis('pub1'))
        self.assertTrue('http://one:1' in rm.subscribers.get_apis('sub1'))
        self.assertTrue('http://one:1' in rm.param_subscribers.get_apis('p1'))
        self.assertTrue('http://one:1' in rm.services.get_apis('s1'))

        # - also, make sure unregister does not erase state if API changed
        rm.unregister_publisher('pub1', 'caller1', 'http://not:1')
        self.assertTrue('http://one:1' in rm.publishers.get_apis('pub1'))
        rm.unregister_subscriber('sub1', 'caller1', 'http://not:1')
        self.assertTrue('http://one:1' in rm.subscribers.get_apis('sub1'))
        rm.unregister_param_subscriber('p1', 'caller1', 'http://not:1')
        self.assertTrue('http://one:1' in rm.param_subscribers.get_apis('p1'))
        rm.unregister_service('sub1', 'caller1', 'rosrpc://not:1')
        self.assertTrue('http://one:1' in rm.services.get_apis('s1'))
        
        
        # erase caller1 sub/srvs/params via register_publisher
        rm.register_publisher('pub1', 'caller1', 'http://newone:1')
        self.assertEqual('http://newone:1', rm.get_node('caller1').api)        
        # - check node ref
        n = rm.get_node('caller1')
        self.assertEqual(['pub1'], n.topic_publications)
        self.assertEqual([], n.services)
        self.assertEqual([], n.topic_subscriptions)
        self.assertEqual([], n.param_subscriptions)
        # - checks publishers
        self.assertTrue('http://newone:1' in rm.publishers.get_apis('pub1'))
        # - checks subscribers
        self.assertTrue(rm.subscribers.has_key('sub1'))
        self.assertFalse('http://one:1' in rm.subscribers.get_apis('sub1'))
        # - checks param subscribers
        self.assertTrue(rm.param_subscribers.has_key('p1'))
        self.assertFalse('http://one:1' in rm.param_subscribers.get_apis('p1'))

        # erase caller2 pub/sub/params via register_service
        # - initial state
        self.assertTrue('http://two:1' in rm.publishers.get_apis('pub1'))
        self.assertTrue('http://two:1' in rm.subscribers.get_apis('sub1'))
        self.assertTrue('http://two:1' in rm.param_subscribers.get_apis('p1'))
        # - change ownership of s1 to caller2
        rm.register_service('s1', 'caller2', 'http://two:1', 'rosrpc://two:1')
        self.assertTrue('http://two:1' in rm.services.get_apis('s1'))
        self.assertTrue('http://two:1' in rm.publishers.get_apis('pub1'))
        self.assertTrue('http://two:1' in rm.subscribers.get_apis('sub1'))
        self.assertTrue('http://two:1' in rm.param_subscribers.get_apis('p1'))
        
        rm.register_service('s1', 'caller2', 'http://newtwo:1', 'rosrpc://newtwo:1')
        self.assertEqual('http://newone:1', rm.get_node('caller1').api)        
        # - check node ref
        n = rm.get_node('caller2')
        self.assertEqual([], n.topic_publications)
        self.assertEqual(['s1'], n.services)
        self.assertEqual([], n.topic_subscriptions)
        self.assertEqual([], n.param_subscriptions)
        # - checks publishers
        self.assertTrue(rm.publishers.has_key('pub1'))
        self.assertFalse('http://two:1' in rm.publishers.get_apis('pub1'))
        # - checks subscribers
        self.assertTrue(rm.subscribers.has_key('sub1'))
        self.assertFalse('http://two:1' in rm.subscribers.get_apis('sub1'))
        self.assertEqual([['sub1', ['caller3']]], rm.subscribers.get_state())
        # - checks param subscribers
        self.assertTrue(rm.param_subscribers.has_key('p1'))
        self.assertFalse('http://two:1' in rm.param_subscribers.get_apis('p1'))
        self.assertEqual([['p1', ['caller3']]], rm.param_subscribers.get_state())

        
    def test_Registrations_unregister_all(self):
        import rosmaster.exceptions
        from rosmaster.registrations import Registrations

        r = Registrations(Registrations.TOPIC_SUBSCRIPTIONS)        
        for k in ['topic1', 'topic1b', 'topic1c', 'topic1d']:        
            r.register(k, 'node1', 'http://node1:5678')
        r.register('topic2', 'node2', 'http://node2:5678')
        r.unregister_all('node1')
        self.assertFalse(not r)
        for k in ['topic1', 'topic1b', 'topic1c', 'topic1d']:        
            self.assertFalse(r.has_key(k))
        self.assertEqual(['topic2'], [k for k in r.iterkeys()])
        
        r = Registrations(Registrations.TOPIC_PUBLICATIONS)        
        for k in ['topic1', 'topic1b', 'topic1c', 'topic1d']:        
            r.register(k, 'node1', 'http://node1:5678')
        r.register('topic2', 'node2', 'http://node2:5678')
        r.unregister_all('node1')
        self.assertFalse(not r)
        for k in ['topic1', 'topic1b', 'topic1c', 'topic1d']:        
            self.assertFalse(r.has_key(k))
        self.assertEqual(['topic2'], [k for k in r.iterkeys()])

        r = Registrations(Registrations.PARAM_SUBSCRIPTIONS)        
        r.register('param2', 'node2', 'http://node2:5678')
        for k in ['param1', 'param1b', 'param1c', 'param1d']:
            r.register(k, 'node1', 'http://node1:5678')
        r.unregister_all('node1')
        self.assertFalse(not r)
        for k in ['param1', 'param1b', 'param1c', 'param1d']:
            self.assertFalse(r.has_key(k))
        self.assertEqual(['param2'], [k for k in r.iterkeys()])
        
        r = Registrations(Registrations.SERVICE)        
        for k in ['service1', 'service1b', 'service1c', 'service1d']:
            r.register(k, 'node1', 'http://node1:5678', 'rosrpc://node1:1234')
        r.register('service2', 'node2', 'http://node2:5678', 'rosrpc://node2:1234')
        r.unregister_all('node1')
        self.assertFalse(not r)
        for k in ['service1', 'service1b', 'service1c', 'service1d']:
            self.assertFalse(r.has_key(k))
            self.assertEqual(None, r.get_service_api(k))
        self.assertEqual(['service2'], [k for k in r.iterkeys()])
        self.assertEqual('rosrpc://node2:1234', r.get_service_api('service2'))

    def _subtest_Registrations_services(self, r):
        import rosmaster.exceptions

        # call methods that use service_api_map, make sure they are guarded against lazy-init
        self.assertEqual(None, r.get_service_api('s1'))
        r.unregister_all('node1')

        # do an unregister first, before service_api is initialized
        code, msg, val = r.unregister('s1', 'caller1', None, 'rosrpc://one:1234')
        self.assertEqual(1, code)
        self.assertEqual(0, val)        

        try:
            r.register('service1', 'node1', 'http://node1:5678')
            self.fail("should require service_api")
        except rosmaster.exceptions.InternalException: pass
        
        r.register('service1', 'node1', 'http://node1:5678', 'rosrpc://node1:1234')
        
        self.assertTrue('service1' in r) # test contains
        self.assertTrue(r.has_key('service1')) # test contains
        self.assertEqual(['service1'], [k for k in r.iterkeys()])
        self.assertEqual(['http://node1:5678'], r.get_apis('service1'))
        self.assertEqual('rosrpc://node1:1234', r.get_service_api('service1'))
        self.assertEqual([('node1', 'http://node1:5678')], r['service1'])
        self.assertFalse(not r) #test nonzero
        self.assertEqual([['service1', ['node1']]], r.get_state())

        r.register('service1', 'node2', 'http://node2:5678', 'rosrpc://node2:1234')
        self.assertEqual(['service1'], [k for k in r.iterkeys()])
        self.assertEqual('rosrpc://node2:1234', r.get_service_api('service1'))
        self.assertEqual(['http://node2:5678'], r.get_apis('service1'))
        self.assertEqual([('node2', 'http://node2:5678')], r['service1'])
        self.assertEqual([['service1', ['node2']]], r.get_state())

        # register a second service
        r.register('service2', 'node3', 'http://node3:5678', 'rosrpc://node3:1234')
        self.assertEqual('rosrpc://node3:1234', r.get_service_api('service2'))
        self.assertEqual(2, len(r.get_state()))
        self.assertTrue(['service2', ['node3']] in r.get_state(), r.get_state())
        self.assertTrue(['service1', ['node2']] in r.get_state())
        
        # register a third service, second service for node2
        r.register('service1b', 'node2', 'http://node2:5678', 'rosrpc://node2:1234')
        self.assertEqual(3, len(r.get_state()))
        self.assertTrue(['service2', ['node3']] in r.get_state())
        self.assertTrue(['service1b', ['node2']] in r.get_state())
        self.assertTrue(['service1', ['node2']] in r.get_state())
        
        # Unregister
        try:
            r.unregister('service1', 'node2', 'http://node2:1234')
            self.fail("service_api param must be specified")
        except rosmaster.exceptions.InternalException: pass
        
        # - fail if service is not known
        code, _, val = r.unregister('unknown', 'node2', 'http://node2:5678', 'rosprc://node2:1234')
        self.assertEqual(0, val)
        # - fail if node is not registered
        code, _, val = r.unregister('service1', 'node3', 'http://node3:5678', 'rosrpc://node3:1234')
        self.assertEqual(0, val)
        # - fail if service API is different
        code, _, val = r.unregister('service1', 'node2', 'http://node2b:5678', 'rosrpc://node3:1234')
        self.assertEqual(0, val)

        # - unregister service2
        code, _, val = r.unregister('service2', 'node3', 'http://node3:5678', 'rosrpc://node3:1234')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertFalse('service2' in r) # test contains
        self.assertFalse(r.has_key('service2')) 
        self.assertTrue('service1' in [k for k in r.iterkeys()])
        self.assertTrue('service1b' in [k for k in r.iterkeys()])
        self.assertEqual([], r.get_apis('service2'))
        self.assertEqual([], r['service2'])
        self.assertFalse(not r) #test nonzero
        self.assertEqual(2, len(r.get_state()))
        self.assertFalse(['service2', ['node3']] in r.get_state())
        
        # - unregister node2
        code, _, val = r.unregister('service1', 'node2', 'http://node2:5678', 'rosrpc://node2:1234')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertFalse('service1' in r) # test contains
        self.assertFalse(r.has_key('service1')) 
        self.assertEqual(['service1b'], [k for k in r.iterkeys()])
        self.assertEqual([], r.get_apis('service1'))
        self.assertEqual([], r['service1'])
        self.assertFalse(not r) #test nonzero
        self.assertEqual([['service1b', ['node2']]], r.get_state())

        code, _, val = r.unregister('service1b', 'node2', 'http://node2:5678', 'rosrpc://node2:1234')
        self.assertEqual(1, code)
        self.assertEqual(1, val)
        self.assertFalse('service1' in r) # test contains
        self.assertFalse(r.has_key('service1')) 
        self.assertEqual([], [k for k in r.iterkeys()])
        self.assertEqual([], r.get_apis('service1'))
        self.assertEqual([], r['service1'])
        self.assertTrue(not r) #test nonzero
        self.assertEqual([], r.get_state())
        
