################################################################################
# Kafka local infra
################################################################################

kafka:
	@docker-compose -f docker/docker-compose-local.yml up -d --remove-orphans

kafka-down:
	@docker-compose -f docker/docker-compose-local.yml down --remove-orphans

################################################################################
# Launch Faust
################################################################################

app:
	@