from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationRunner
from os import environ

class SkyAgent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def oncounter(count):
            print("event received: {0}", count)

        try:
            yield self.subscribe(oncounter, u'0242ac1a0096.sessions')
            yield self.subscribe(oncounter, u'0242ac1a0096.config')
            yield self.subscribe(oncounter, u'sky.skywifi.0242ac1a0096.status')
            print("subscribed to topic")

        except Exception as e:
            print("could not subscribe to topic: {0}".format(e))

        self.publish(u'sky.skywifi.0242ac1a0096.status',
                ["hello"],
            );
        self.publish(u'sky.skywifi.0242ac1a0096.other',
                ["world"],
            );
runner = ApplicationRunner(url=u"ws://lk.skywifi.pro:8080", realm=u"sky")
runner.run(SkyAgent)
