################################################################################
# Kafka local infra
################################################################################

kafka:
	@docker-compose -f docker/docker-compose-local.yml up -d --remove-orphans --renew-anon-volumes --force-recreate

kafka-down:
	@docker-compose -f docker/docker-compose-local.yml down --remove-orphans

################################################################################
# Launch Faust
################################################################################

app:
	@python 