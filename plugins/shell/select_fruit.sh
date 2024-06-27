FLUIT=$1
if [ $FLUIT == APPLE ];then
	echo "You selected Apple!"
elif [ $FLUIT == ORANGE ];then
        echo "You selected Orange!"
elif [ $FLUIT == GRAPE ];then
        echo "You selected Grape!"
else
        echo "You selected Other!"
fi
