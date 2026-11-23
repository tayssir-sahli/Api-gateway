
const app = require('./app');
const eurekaClient = require('./config/eureka');

const PORT = process.env.PORT || 8083;

// Démarrage du serveur Express
const server = app.listen(PORT, () => {
  console.log(`meeting microservice running on http://localhost:${PORT}`);
  console.log(`Swagger UI: http://localhost:${PORT}/swagger-ui`);

  // Enregistrement auprès de Eureka
  eurekaClient.start((error) => {
    if (error) {
      console.error('Eureka registration failed:', error);
    } else {
      console.log('MEETING successfully registered in Eureka');
    }
  });
});

// Arrêt propre du microservice
process.on('SIGINT', () => {
  console.log('Stopping meeting microservice...');

  eurekaClient.stop(() => {
    console.log('MEETING unregistered from Eureka');

    server.close(() => {
      console.log('Meeting server stopped');
      process.exit(0);
    });
  });
});
