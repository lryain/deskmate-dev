#!/bin/bash

VersionFileName=$1


# helper function to output data into a file
generateVersion() {
  VersionFileName=$1
  Major=$2
  Minor=$3
  Release=$4
  Revision=$5
  Commit=$6
  DasUser=$7
  echo $Major.$Minor.$Release.$Revision.$Commit
  echo "//autogenerated do not edit by hand" > $VersionFileName
  echo "#define BASESTATION_VERSION \"$Major.$Minor.$Release.$Revision.$Commit\"" >> $VersionFileName
  echo "#define BASESTATION_VERSION_MAJOR $Major" >> $VersionFileName
  echo "#define BASESTATION_VERSION_MINOR $Minor" >> $VersionFileName
  echo "#define BASESTATION_VERSION_RELEASE $Release" >> $VersionFileName
  echo "#define BASESTATION_VERSION_REVISION $Revision" >> $VersionFileName
  echo "#define BASESTATION_VERSION_COMMIT \"$Commit\"" >> $VersionFileName
  echo "#define DAS_USER \"$DasUser\"" >> $VersionFileName
}



# find git
GIT=`which git`
if [ -z $GIT ]
then
  echo git not found
  exit 1
fi
TOPLEVEL=`$GIT rev-parse --show-toplevel`

# build version file name
if [ -z $VersionFileName ]; then
  VersionFileName=$TOPLEVEL/source/anki/basestation/version.h
fi


# find user source and parse it
VersionSource=$TOPLEVEL/source/anki/basestation/VERSION
UserDefinedVersion=`cat $VersionSource`
a=( ${UserDefinedVersion//./ } )
Major=${a[0]}
Minor=${a[1]}
Release=${a[2]}
Commit=`$GIT rev-parse --short HEAD`

# parse previous version info
VersionDataFileName=$TOPLEVEL/tools/build/versionGenerator/versionData.txt
PreviousVersion=`head -1 $VersionDataFileName`
PreviousCommit=`tail -1 $VersionDataFileName`

#echo $PreviousVersion  $PreviousCommit
# create revision number
Revision=`$GIT log --oneline $PreviousCommit.. | wc -l | tr -d ' '`

# save current version data into the file
if [ $PreviousVersion != $UserDefinedVersion ]; then
  echo new version detected
  Revision="0"
  echo $Major.$Minor.$Release > $VersionDataFileName
  echo $Commit >> $VersionDataFileName
fi


DasUser=`whoami`
# create file if it does not exist
if [ ! -f $VersionFileName ]; then
  echo version file created
  generateVersion $VersionFileName $Major $Minor $Release $Revision $Commit $DasUser
  exit 0
fi

newVersion=$Major.$Minor.$Release.$Revision.$Commit

# parse old version . h and compare the data
oldVersion=`head -2 $VersionFileName | tail -1 | cut -d ' ' -f 3`
oldVersion="${oldVersion%\"}"
oldVersion="${oldVersion#\"}"
egrep -q "DAS_USER \"$DasUser\"" $VersionFileName
if [ "$oldVersion" != "$newVersion" -o $? -ne 0 ];then
  echo "[anki-util] version file updated"
  generateVersion $VersionFileName $Major $Minor $Release $Revision $Commit $DasUser
  exit 0
fi


echo "[anki-util] version file ok"
exit 0