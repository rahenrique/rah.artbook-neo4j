help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

down: ## Destroy all dependencies
	@echo "Makefile: Stoping and removing container..."
	@docker-compose down --v

	@echo "Makefile: Listing containers..."
	@docker ps

run: ## Start and run the application
	@echo "Makefile: Starting container..."
	@docker-compose up -d
	@docker ps

exec: ## Open container interactive pseudo tty
	@echo "Makefile: Opening container interactive pseudo tty..."
	@docker exec -it artbook-app /bin/bash

init: ## Setup dependencies to run the application for the first time
	@echo "Makefile: Creating and starting container..."
	@docker-compose up -d --build --force-recreate

	@echo "Makefile: Listing containers..."
	@docker ps

log: ## Log container's stdout
	@echo "Makefile: Logging container's stdout..."
	@docker logs -f artbook-app

test: ## Run tests with pytest
	@docker exec -it artbook-app pytest -v -p no:cacheprovider