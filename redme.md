## kafka cli cmds (see kafka-cli docs)
# inside kafka docker container
kafka-topics --list --bootstrap-server localhost:9092
kafka-topics --bootstrap-server localhost:9092 --describe --topic orders
kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning