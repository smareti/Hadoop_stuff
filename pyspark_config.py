# Set up spark configuration
	conf = SparkConf().setMaster("yarn-client").setAppName("sparK-mer")
	#conf = SparkConf().setMaster("local[16]").setAppName("sparK-mer")
	conf.set("yarn.nodemanager.resource.cpu_vcores",args.C)
	# Saturate with executors
	conf.set("spark.executor.instances",executorInstances)
	conf.set("spark.executor.heartbeatInterval","5s")
	# cores per executor
	conf.set("spark.executor.cores",args.E)
	# set driver cores
	conf.set("spark.driver.cores",12)
	# Number of akka threads
	conf.set("spark.akka.threads",256)
	# Agregation worker memory
	conf.set("spark.python.worker.memory","5g")
	# Maximum message size in MB
	conf.set("spark.akka.frameSize","128")
	conf.set("spark.akka.timeout","200s")
	conf.set("spark.akka.heartbeat.interval","10s")
	#conf.set("spark.broadcast.blockSize","128m")
	conf.set("spark.driver.maxResultSize", "20g")
	conf.set("spark.reducer.maxSizeInFlight","5g")
	conf.set("spark.executor.memory","7g")
	#conf.set("spark.shuffle.memoryFraction",0.4)
	#conf.set("spark.storage.memoryFraction",0.3)
	#conf.set("spark.storage.unrollFraction",0.3)
	#conf.set("spark.storage.memoryMapThreshold","256m")
	#conf.set("spark.kryoserializer.buffer.max","1g")
	#conf.set("spark.kryoserializer.buffer","128m")
	#conf.set("spark.core.connection.ack.wait.timeout","600")
	#conf.set("spark.shuffle.consolidateFiles","true")
	#conf.set("spark.shuffle.file.buffer","32m")
	conf.set("spark.shuffle.manager","sort")
	conf.set("spark.shuffle.spill","true")

	# Set up Spark Context
	sc = SparkContext("","",conf=conf)
	#sc.setLogLevel(args.L)
