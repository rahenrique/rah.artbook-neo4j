.PHONY: help down run exec init log test
.DEFAULT_GOAL := help

help: ## Prints this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

rah: ## Simple test
ifdef param
	@echo "Recebido param='${param}'"
	@echo $(param)
else
	@echo "ERROR: Missing required parameter 'param'..."
endif

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
	@echo "Makefile: Copying .env file from sample..."
	@cp -v $(shell pwd)/app/.env.example $(shell pwd)/app/.env

	@echo "Makefile: Creating and starting container..."
	@docker-compose up -d --build --force-recreate

	@echo "Makefile: Listing containers..."
	@docker ps

log: ## Log container's stdout
	@echo "Makefile: Logging container's stdout..."
	@docker logs -f artbook-app

test: ## Run tests with pytest
	@docker exec -it artbook-app pytest -v -p no:cacheprovider