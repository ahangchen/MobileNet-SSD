data_dir="/opt/movidius/ssd-caffe/data/coco_cattle"
example_dir="/opt/movidius/ssd-caffe/examples/MobileNet-SSD"

rm -rf $data_dir/Annotations
rm -rf $data_dir/images
rm -rf $data_dir/ImageSets

mv $example_dir/data/Annotations $data_dir/
mv $example_dir/data/images $data_dir/
mv $example_dir/data/ImageSets $data_dir/

echo "mv file to data/coco_cattle"

cp $data_dir/Annotations/0* $data_dir/all/
cp $data_dir/Annotations/1* $data_dir/all/
cp $data_dir/Annotations/2* $data_dir/all/
cp $data_dir/Annotations/3* $data_dir/all/
cp $data_dir/Annotations/4* $data_dir/all/
cp $data_dir/Annotations/5* $data_dir/all/
cp $data_dir/Annotations/6* $data_dir/all/
cp $data_dir/Annotations/7* $data_dir/all/
cp $data_dir/Annotations/8* $data_dir/all/
cp $data_dir/Annotations/9* $data_dir/all/
echo "cp Annotations to all"
cp $data_dir/images/0* $data_dir/all/
cp $data_dir/images/1* $data_dir/all/
cp $data_dir/images/2* $data_dir/all/
cp $data_dir/images/3* $data_dir/all/
cp $data_dir/images/4* $data_dir/all/
cp $data_dir/images/5* $data_dir/all/
cp $data_dir/images/6* $data_dir/all/
cp $data_dir/images/7* $data_dir/all/
cp $data_dir/images/8* $data_dir/all/
cp $data_dir/images/9* $data_dir/all/
echo "cp images to all"

cd $data_dir && ./create_data.sh
cd $example_dir

rm $example_dir/trainval_lmdb
rm $example_dir/test_lmdb
ln -s $data_dir/lmdb/coco_cattle_train_lmdb $example_dir/trainval_lmdb
ln -s $data_dir/lmdb/coco_cattle_test_lmdb $example_dir/test_lmdb
echo "ln to coding dir"