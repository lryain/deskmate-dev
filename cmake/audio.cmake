#
# Link Audio Plugins
#

option(AUDIO_RELEASE "Only link plugs we have licensed for" OFF)

if(AUDIO_RELEASE)
  # Only link plugins we have lisences for
  message(STATUS "AUDIO_RELEASE is ON - Only link licensed plugins")
  set(LRYA_LIB_AUDIO_PLUGINS
    # Effect Plugins
    AE_AK_COMPRESSOR_FX
    AE_AK_DELAY_FX
    AE_AK_METER_FX
    AE_AK_EXPANDER_FX
    AE_AK_PARAMETRIC_EQ_FX
    AE_AK_GAIN_FX
    AE_AK_PEAK_LIMITER_FX
    AE_AK_PITCH_SHIFTER_FX
    AE_AK_TIME_STRETCH_FX
    AE_AK_FLANGER_FX
    AE_AK_TREMOLO_FX
    AE_AK_HARMONIZER_FX
    AE_AK_MATRIX_REVERB_FX
    AE_AK_ROOM_VERB_FX
    AE_AK_GUITAR_DISTORTION_FX
    AE_AK_STEREO_DELAY_FX
    AE_AK_RECORDER_FX
    AE_MCDSP_LIMITER_FX
    AE_Krotos_Vocoder_FX
    # Source Plugins
    AE_AK_SILENCE_SOURCE
    AE_AK_SINE_GENERATOR_SOURCE
    AE_AK_TONE_GENERATOR_SOURCE
    AE_AK_SYNTH_ONE_SOURCE
  )

  if(MATEOS)
  list(APPEND LRYA_LIB_AUDIO_PLUGINS
    # Sink Plugins
    AE_AK_ALSA_SINK
  )
  endif(MATEOS)

else()

  # Link all availble plugins
  message(STATUS "AUDIO_RELEASE is OFF - Link all Wwise plugins")
  set(LRYA_LIB_AUDIO_PLUGINS
    # Effect Plugins
    AE_AK_COMPRESSOR_FX
    AE_AK_DELAY_FX
    AE_AK_METER_FX
    AE_AK_EXPANDER_FX
    AE_AK_PARAMETRIC_EQ_FX
    AE_AK_GAIN_FX
    AE_AK_PEAK_LIMITER_FX
    AE_AK_PITCH_SHIFTER_FX
    AE_AK_TIME_STRETCH_FX
    AE_AK_FLANGER_FX
    AE_AK_TREMOLO_FX
    AE_AK_HARMONIZER_FX
    AE_AK_MATRIX_REVERB_FX
    AE_AK_ROOM_VERB_FX
    AE_AK_SOUND_SEED_IMPACT_FX
    AE_AK_GUITAR_DISTORTION_FX
    AE_AK_STEREO_DELAY_FX
    AE_AK_CONVOLUTION_REVERB_FX
    AE_AK_RECORDER_FX
    AE_MCDSP_LIMITER_FX
    AE_MCDSP_FUTZ_BOX_FX
    AE_Krotos_Vocoder_FX
    # Source Plugins
    AE_AK_SILENCE_SOURCE
    AE_AK_SINE_GENERATOR_SOURCE
    AE_AK_TONE_GENERATOR_SOURCE
    AE_AK_SOUND_SEED_WOOSH_SOURCE
    AE_AK_SOUND_SEED_WIND_SOURCE
    AE_AK_SYNTH_ONE_SOURCE
  )

  if(MATEOS)
  list(APPEND LRYA_LIB_AUDIO_PLUGINS
    # Sink Plugins
    AE_AK_ALSA_SINK

    # Linux specific plugins
    AE_iZotope_HybridReverb_FX
    AE_iZotope_TrashBoxModeler_FX
    AE_iZotope_TrashDelay_FX
    AE_iZotope_TrashDistortion_FX
    AE_iZotope_TrashDynamics_FX
    AE_iZotope_TrashFilters_FX
    AE_iZotope_TrashMultibandDistortion_FX
  )
  endif(MATEOS)

endif(AUDIO_RELEASE)

import(audio "lib/audio")
