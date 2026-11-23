
const Eureka = require('eureka-js-client').Eureka;

const PORT = process.env.PORT || 8083;

const client = new Eureka({
    instance: {
        app: 'MEETING',
        instanceId: `MEETING:${PORT}`,
        hostName: 'localhost',
        ipAddr: '127.0.0.1',
        statusPageUrl: `http://localhost:${PORT}`,
        healthCheckUrl: `http://localhost:${PORT}/api/meetings/hello`,
        port: {
            '$': PORT,
            '@enabled': true
        },
        vipAddress: 'MEETING',
        dataCenterInfo: {
            '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
            name: 'MyOwn'
        }
    },

    eureka: {
        host: 'localhost',
        port: 8761,
        servicePath: '/eureka/apps/'
    },

    requestMiddleware: (requestOpts, done) => {
        requestOpts.auth = {
            user: process.env.EUREKA_USERNAME,
            password: process.env.EUREKA_PASSWORD
        };
        done(requestOpts);
    }
});

module.exports = client;
