build:
	docker build -t my-router ./router
	docker build -t my-python-executor ./python-executor
	docker build -t my-java-executor ./java-executor
	docker build -t my-dart-executor ./dart-executor

run:
	docker run -d -p 5000:5000 server
	docker run -d -p 5001:5001 python-executor
	docker run -d -p 5002:5002 java-executor
	docker run -d -p 5003:5003 dart-executor

stop:
	docker stop $$(docker ps -q --filter ancestor=router)
	docker stop $$(docker ps -q --filter ancestor=python-executor)
	docker stop $$(docker ps -q --filter ancestor=java-executor)
	docker stop $$(docker ps -q --filter ancestor=dart-executor)

rebuild: stop build run
