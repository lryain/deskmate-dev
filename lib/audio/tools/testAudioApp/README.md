# Test Audio App

This is a standalone command line app to test Anki's Audio Library. The app is project independent allowing the user to use any sound bank and configuration file. Anki uses [Audio Kinetic Wwise](https://www.audiokinetic.com) as the our audio engine middleware therefore sound banks must be generated by Wwise's Authoring tool. To configure and perform audio tasks we leverage our [Audio Scene Object](https://ankiinc.atlassian.net/wiki/spaces/AUD/pages/144351552/Audio+Scene+Metadata), which can be loaded as a JSON file. The app will perform each audio tasks in the order it is listed in the audio scene file. Run the app's help `-h` for details.


##Build
Due to linking complexities the easiest way to build by using Victor's `build-victor.sh` script. To build `test_audio_app` enable CMake option `BUILD_TEST_AUDIO_APP`. From victor repo root run `./project/victor/build-victor.sh -a -DBUILD_TEST_AUDIO_APP=ON` Use victor's deploy scripts to copy app to the robot `./project/victor/scripts/deploy.sh`. The app will be in `com.anki.cozmoengine/bin` directory.


##Run
To run on the app on the robot you need to set the shared library path. For example `LD_LIBRARY_PATH=/data/data/com.anki.cozmoengine/lib /data/data/com.anki.cozmoengine/bin/test_audio_app`