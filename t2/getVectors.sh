mkdir vectors
cd vectors
wget "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ru.300.bin.gz"
wget "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.be.300.bin.gz"
gzip -d cc*
