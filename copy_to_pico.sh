DEST="/d/"
cp reset.bat code.py code-default.py code-steamworkshop-example.py $DEST
mkdir $DEST/lib >/dev/null 2>&1
cp lib/* $DEST/lib/
mkdir $DEST/Save >/dev/null 2>&1
cp Save/* $DEST/Save/ 
