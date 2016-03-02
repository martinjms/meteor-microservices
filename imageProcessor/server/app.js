Cluster.connect('mongodb://127.0.0.1/cluster');

Cluster.register('imageProcessor');

biotools = Cluster.discoverConnection('biotools');
