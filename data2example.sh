data_dir="/opt/movidius/ssd-caffe/data/coco_cattle"
example_dir="/opt/movidius/ssd-caffe/examples/MobileNet-SSD"

cp $example_dir/data/Annotations/* $data_dir/Annotations/
cp $example_dir/data/images/* $data_dir/images/
cp $example_dir/data/ImageSets/* $data_dir/ImageSets/
cp $data_dir/Annotations/* $data_dir/all/
cp $data_dir/images/* $data_dir/all/
cd $data_dir && ./create_data.sh
cd $example_dir
ln -s $data_dir/lmdb/coco_cattle_train_lmdb $example_dir/trainval_lmdb
ln -s $data_dir/lmdb/coco_cattle_test_lmdb $example_dir/test_lmdb
