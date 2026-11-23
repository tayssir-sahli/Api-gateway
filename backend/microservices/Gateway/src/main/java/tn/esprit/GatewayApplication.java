package tn.esprit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.cloud.loadbalancer.annotation.LoadBalancerClient;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@EnableDiscoveryClient
@LoadBalancerClient(name = "candidat", configuration = CandidatLoadBalancerConfig.class)
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }

   /* @Bean
    public RouteLocator gatewayRoutes(RouteLocatorBuilder builder) {
        return builder.routes()
                .route("Candidat", r -> r.path("/api/candidates/**", "/api/addresses/**")
                        .uri("http://localhost:8081"))
                .route("Job", r -> r.path("/api/jobs/**", "/api/categories/**")
                        .uri("http://localhost:8082"))
                .build();
    }*/


  /*  @Bean
    public RouteLocator gatewayRoutes(RouteLocatorBuilder builder) {
        return builder.routes()
                .route("Candidat", r -> r.path("/api/candidates/**", "/api/addresses/**")
                        .uri("lb://candidat"))
                .route("Job", r -> r.path("/api/jobs/**", "/api/categories/**")
                        .uri("lb://job"))
                .build();
    }*/
}