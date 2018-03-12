data_dir="/opt/movidius/ssd-caffe/data/coco_cattle"
example_dir="/opt/movidius/ssd-caffe/examples/MobileNet-SSD"

cd $example_dir
ln -s $data_dir/lmdb/coco_cattle_train_lmdb $example_dir/trainval_lmdb
ln -s $data_dir/lmdb/coco_cattle_test_lmdb $example_dir/test_lmdb
