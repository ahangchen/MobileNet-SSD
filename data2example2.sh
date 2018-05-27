data_dir="/opt/movidius/ssd-caffe/data/coco_cattle"
example_dir="/opt/movidius/ssd-caffe/examples/MobileNet-SSD"

cd $data_dir && ./create_data.sh
cd $example_dir

rm $example_dir/trainval_lmdb
rm $example_dir/test_lmdb
ln -s $data_dir/lmdb/coco_cattle_train_lmdb $example_dir/trainval_lmdb
ln -s $data_dir/lmdb/coco_cattle_test_lmdb $example_dir/test_lmdb
echo "ln to coding dir"