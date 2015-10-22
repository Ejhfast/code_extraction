# python path import collision
cp -r ./examples/utils/ ./examples/xutils/
rm -R ./examples/utils/utils
find ./ -type f -exec sed -i 's/examples.utils/examples.xutils/g'  {} \;
