#ifndef __BB_BABILE__IC_BABILE_H__
#define __BB_BABILE__IC_BABILE_H__


#define BABILE_SEL_MINOUTBUFFERSIZE		2048
#define BABILE_MBR_MINOUTBUFFERSIZE		512

/*C# Wrapper: public enum BABILE_LANGUAGE_CODE : short {*/
/* Language codes */
#define BABILE_LANGUAGE_CODE_DEFAULT	0x3256	/*2V*/
#define BABILE_LANGUAGE_CODE_ARM		0x3356	/*3V*/
#define BABILE_LANGUAGE_CODE_CZC		0x3456	/*4V*/
#define BABILE_LANGUAGE_CODE_DUB		0x3556	/*5V*/
#define BABILE_LANGUAGE_CODE_DUN		0x3656	/*6V*/
#define BABILE_LANGUAGE_CODE_ENG		0x3756	/*7V*/
#define BABILE_LANGUAGE_CODE_ENU		0x3856	/*8V*/
#define BABILE_LANGUAGE_CODE_FRF		0x3956 	/*9V*/
#define BABILE_LANGUAGE_CODE_DAD		0x3a56	/*:V*/
#define BABILE_LANGUAGE_CODE_NON		0x3b56	/*;V*/
#define BABILE_LANGUAGE_CODE_FIF		0x3c56	/*<V*/
#define BABILE_LANGUAGE_CODE_SPM		0x3d56	/**/
#define BABILE_LANGUAGE_CODE_SPU		0x3e56	/**/
#define BABILE_LANGUAGE_CODE_RUR		0x3f56	/**/
#define BABILE_LANGUAGE_CODE_GED		0x4056	/*@V*/
#define BABILE_LANGUAGE_CODE_GRG		0x4156	/*AV*/
#define BABILE_LANGUAGE_CODE_ISI		0x4256	/*BV*/
#define BABILE_LANGUAGE_CODE_ITI		0x4356	/*CV*/
#define BABILE_LANGUAGE_CODE_POB		0x4456	/*DV*/
#define BABILE_LANGUAGE_CODE_POE		0x4556	/*EV*/
#define BABILE_LANGUAGE_CODE_SPS		0x4656	/*FV*/
#define BABILE_LANGUAGE_CODE_SWS		0x4756	/*GV*/
#define BABILE_LANGUAGE_CODE_TUT		0x4856	/*HV*/
#define BABILE_LANGUAGE_CODE_FRC		0x4956	/**/
#define BABILE_LANGUAGE_CODE_FAF		0x4a56 /*JV*/
#define BABILE_LANGUAGE_CODE_POP		0x4b56	/**/
#define BABILE_LANGUAGE_CODE_HUH		0x4c56	/**/
#define BABILE_LANGUAGE_CODE_EN_IN		0x4d56	/**/
#define BABILE_LANGUAGE_CODE_CA_ES		0x4e56	/**/
#define BABILE_LANGUAGE_CODE_JA_JP		0x4f56	/**/
#define BABILE_LANGUAGE_CODE_ZH_CN		0x5056	
#define BABILE_LANGUAGE_CODE_SV_FI		0x5156	/*HV*/
#define BABILE_LANGUAGE_CODE_SC_SE		0x5256	
#define BABILE_LANGUAGE_CODE_GB_SE		0x5356	
#define BABILE_LANGUAGE_CODE_EN_AU		0x5456	
#define BABILE_LANGUAGE_CODE_KO_KR		0x5556
#define BABILE_LANGUAGE_CODE_FO_FO		0x5656
#define BABILE_LANGUAGE_CODE_NS_SAM		0x5756
/*C# Wrapper: } BABILE_LANGUAGE_CODE */

/*C# Wrapper: public enum BABILE_ERROR : int {*/
/* BABILE errors */
#define E_BABILE_NOVALIDSYNTH		-48
#define E_BABILE_COLINITERROR		-47
#define E_BABILE_NOCOLIBRI			-46
#define E_BABILE_COLERROR			-45
#define E_BABILE_NLPERROR			-44
#define E_BABILE_NOMBR				-43
#define E_BABILE_PHONBUFERROR		-42
#define E_BABILE_SYNTHESIZESF		-41
#define E_BABILE_LICENSE			-34
#define E_BABILE_NOSEL				-33
#define E_BABILE_SELERROR			-32
#define E_BABILE_SELINITERROR		-31
#define E_BABILE_DICT_EXIST			-30
#define E_BABILE_PHOSTRPROGRESSERROR	-29
#define E_BABILE_MBRERROR			-28
#define E_BABILE_NLPINITERROR		-27
#define E_BABILE_MBRINITERROR		-26
#define E_BABILE_NULLARG				-25
#define E_BABILE_VALUEOUTOFBOUNDS	-24		/* BABILE */
#define E_BABILE_NODICT				-23
#define E_BABILE_NODBA				-22		/* database ERROR */
#define E_BABILE_NOTIMPLEMENTED		-21
#define E_BABILE_DICT_NOENTRY		-20
#define E_BABILE_DICT_READ			-19	
#define E_BABILE_DICT_WRITE			-18
#define E_BABILE_DICT_OPEN			-17
#define E_BABILE_BADPHO				-16
#define E_BABILE_FILEOPEN			-15
#define E_BABILE_FILEWRITE			-14
#define E_BABILE_INVALIDTAG			-13
#define E_BABILE_NONLP				-12
#define E_BABILE_THREADERROR			-11
#define E_BABILE_NOTVALIDPARAMETER	-10
#define E_BABILE_NOREGISTRY			-9		/* Registry keys error*/
#define E_BABILE_REGISTRYERROR		-8
#define E_BABILE_PROCESSERROR		-7
#define E_BABILE_WAVEOUTNOTFREE		-6		/* Can't open the wavout device */
#define E_BABILE_WAVEOUTWRITE		-5
#define E_BABILE_SPEAKERROR			-4		/* Error while Speaking or processing text */
#define E_BABILE_ISPLAYING			-3		/* already in play mode or currently processing text */
#define E_BABILE_MEMFREE				-2		/* problem when deallocating */ 
#define E_BABILE_NOMEM				-1		/* no memory for allocation */
#define E_BABILE_NOERROR				 0		/* no error */
#define W_BABILE_NOTPROCESSED			1
#define W_BABILE_FORCEDTOFLUSH			2
#define W_BABILE_NEEDMORE				3
/*C# Wrapper: } BABILE_ERROR*/

/*C# Wrapper:    public enum BABILE_Param : int { */
/* Babile Parameters (BABILE_Param) */
#define BABIL_PARM_PITCH			2 /*NLPE_PARM_PITCH*/
#define BABIL_PARM_SPEED			3 /*NLPE_PARM_SPEED*/
#define BABIL_PARM_WAVEFORMAT		4
#define BABIL_PARM_VOICEFREQ		5
#define BABIL_PARM_FILEFORMAT		6
#define	BABIL_PARM_MAXSENTENCE		7
#define BABIL_PARM_NOTIFWND			8
#define BABIL_PARM_MAXPITCH			9 /*NLPE_PARM_MAXPITCH*/
#define BABIL_PARM_MINPITCH			10 /*NLPE_PARM_MINPITCH*/
#define BABIL_PARM_VOLUMERATIO		11
#define BABIL_MINVOL	0
#define BABIL_MAXVOL	899
#define BABIL_PARM_CBINSTANCE		12
#define BABIL_PARM_LEADINGSILENCE	13 /*NLPE_PARM_LEADINGSILENCE*/
/*#define BABIL_PARM_MIDDLESILENCE	14 *//*NLPE_PARM_MIDDLESILENCE */
#define BABIL_PARM_TRAILINGSILENCE	15 /*NLPE_PARM_TRAILINGSILENCE*/
#define BABIL_PARM_DEVICE			16
#define BABIL_PARM_MSGMASK			17
#define BABIL_PARM_ABSSPEED			18
#define BABIL_PARM_ACTIVEMODULES	19
#define BABIL_PARM_SENTENCELENGTH	20
#define BABIL_PARM_VAL_SENTENCE_EXTRALONG		9
#define BABIL_PARM_VAL_SENTENCE_LONG			8
#define BABIL_PARM_VAL_SENTENCE_MED				7
#define BABIL_PARM_VAL_SENTENCE_SHORT			6
#define BABIL_PARM_VAL_SENTENCE_EXTRASHORT		5
#define BABIL_PARM_PAUSE1SILENCE	21 /*NLPE_PARM_PAUSE1SILENCE*/
#define BABIL_PARM_PAUSE2SILENCE	22 /*NLPE_PARM_PAUSE2SILENCE*/
#define BABIL_PARM_PAUSE3SILENCE	23 /*NLPE_PARM_PAUSE3SILENCE*/
#define BABIL_PARM_PAUSE4SILENCE	24 /*NLPE_PARM_PAUSE4SILENCE*/
#define BABIL_PARM_PAUSE5SILENCE	25 /*NLPE_PARM_PAUSE5SILENCE*/
#define BABIL_PARM_LOS_THRESHOLD	26 /*NLPE_PARM_LOS_THRESHOLD*/
#define BABIL_PARM_LOS_WORD_THRESHOLD	27 /*NLPE_PARM_LOS_WORD_THRESHOLD*/
#define BABIL_PARM_MAXEXTF0			30 /*NLPE_PARM_MAXEXTF0*/
#define BABIL_PARM_MAXINTF0			31 /*NLPE_PARM_MAXINTF0*/
#define BABIL_PARM_WORDSPELLVOIRATIO 32 /*NLPE_PARM_WORDSPELLVOIRATIO*/
#define BABIL_PARM_ACROSPELLCONRATIO 33 /*NLPE_PARM_ACROSPELLCONRATIO*/
/* reserved							 34 */
/* reserved							 35 */
/* reserved							 36 */
#define BABIL_PARM_PTR_DCTCALLOBJ	37
#define BABIL_PARM_PTR_DCTCALLFCT	38
/* reserved							39	*/
#define BABIL_PARM_LANGUAGECODE		40 /*BBNLP_PARAM_LANGUAGECODE*/
#define BABIL_PARM_SPEAKON			41
#define BABIL_PARM_VAL_SPEAKONTEXT	0
#define BABIL_PARM_VAL_SPEAKONWORD	1
#define BABIL_PARM_VAL_SPEAKONCHAR	2
#define BABIL_PARM_VAL_SPEAKONIWOR	3
#define BABIL_PARM_DCTORDER			42
#define BABIL_PARM_VAL_DCTORDER_CUS	0	/*default*/	/* 1:callback, 2:user, 3:system */
#define BABIL_PARM_VAL_DCTORDER_USC	1				/* 1:user, 2:system, 3:callback */
/*#define BABIL_PARM_VAL_DCTORDER_SCU	2			*/	/* 1:system, 2:callback, 3:user */
/*#define BABIL_PARM_VAL_DCTORDER_CSU	3			*/
/*#define BABIL_PARM_VAL_DCTORDER_UCS	4			*/
/*#define BABIL_PARM_VAL_DCTORDER_SUC	5			*/
/* reserved                             43  */
#define BABIL_PARM_PTR_TAGCALLFCT	45  
#define BABIL_PARM_PTR_TAGCALLOBJ	46  
/* reserved                             47  */
#define BABIL_PARM_PTR_MARKCB       48  /* provide Mark callback through babileParams structure */
#define BABIL_PARM_SYNC				49
#define BABIL_PARM_VAL_SYNCONWORDS	0x0002		/* sync on words */

/* MBROLA/E SYNTHESIZER OPTIONS:*/
#define BABIL_PARM_MBR_FREQ			50
#define BABIL_PARM_MBR_PITCH		52
#define BABIL_PARM_MBR_TIME			53
#define BABIL_PARM_MBR_SMOO			54
#define BABIL_PARM_MBR_SYNC			55
#define BABIL_PARM_MBR_VAL_SEL_SYNCONWORDS	0x0002		/* sync on words */
#define BABIL_PARM_MBR_VOICEFREQ	56 /* Voice Frequency */
#define BABIL_PARM_SEL_NBPRESEL		60
/*#define BABIL_PARM_SEL_PHOCONTEXT	61*/
#define BABIL_PARM_SEL_SYNC			63
#define BABIL_PARM_SEL_VAL_SYNCONPHONEMES	0x0001		/* sync on ponemes */
#define BABIL_PARM_SEL_VAL_MBR_SYNCONWORDS	0x0002		/* sync on words */
#define BABIL_PARM_SEL_VAL_SYNCONBREATHG	0x0004		/* sync on breath groups */
#define BABIL_PARM_SEL_VAL_SYNCONSENTENCE	0x0008		/* sync on sentences */
#define BABIL_PARM_SEL_VAL_SYNCONDURCALL	0x0010		/* sync on ??? reserved for BABTTS */
#define BABIL_PARM_SEL_VAL_SYNCONDIPHONES	0x0020		/* sync on Diphones */
#define BABIL_PARM_SEL_VOICEFREQ	64
#define BABIL_PARM_SEL_PITCH		65
#define BABIL_PARM_SEL_TIME			66	
#define BABIL_PARM_SEL_VOICECTRL	67  /*HNM*/
#define BABIL_PARM_SEL_VOICESHAPE	68
#define BABIL_PARM_SEL_SELBREAK	69
#define BABIL_PARM_SEL_RESERVED1	70
#define BABIL_PARM_SEL_RESERVED2	71 /* special, only for Harmoniser */
#define BABIL_PARM_SEL_RESERVED3	72 /* special, only for Harmoniser */
#define BABIL_PARM_SEL_RESERVED4	73 /* special, only for Harmoniser */
#define BABIL_PARM_SEL_SPANAROUNDVOICEPITCHDELTA 74 /* special */
#define BABIL_PARM_PITCHNLP			75	/* control NLP pitch rather than synthesizer's  */
#define BABIL_PARM_SAMPLESIZE		76 
#define BABIL_PARM_AUDIOBOOST_PREEMPH			77
#define BABIL_PARM_PTR_MARKCBOBJ    80  /* provide Mark callback object */
#define BABIL_PARM_COL_WARPING		81
#define BABIL_PARM_CODEPAGE			91
/*C# Wrapper: } BABILE_Param */

/* Babile Pho Modes (BABILE_PhoMode) */
#define BABILE_ONLYPHO				0	/* -= onlypho*/
#define BABILE_NORMALPHO			1	/* normal pho */
#define BABILE_DLSTTS				2	/* don't use it!!! */
#define BABILE_MARKPHO				3	/* normal pho + word sync */
#define BABILE_BINNORMALPHO			4	/* bin normal pho */
#define BABILE_BINMARKPHO			5	/* bin normal pho + word sync */
#define BABILE_TEXTPHONETIZE		6	/* (phonetizer mode) == BABILE_MARKPHO + BABILE_PHONETIZE */
#define BABILE_BINONLYPHO			7	/* bin only pho */

#define BABILE_PHONETIZE_MASK		0x07
#define BABILE_PHONETIZE			0x08	/* (phonetizer mode) */

#define BABILE_MBRE_BUFFERING10		10			
#define BABILE_MBRE_BUFFERING5		5		

#define	BABILE_SEL_BUFFERING10			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_ALL  |BUFFER_BERSTREAM_ALL
#define	BABILE_SEL_BUFFERING10F			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_ALL  |BUFFER_BERSTREAM_ALL  |BUFFER_FORCE
#define	BABILE_SEL_BUFFERING8			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_ALL
#define	BABILE_SEL_BUFFERING8F			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_ALL  |BUFFER_FORCE
#define	BABILE_SEL_BUFFERING7			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_SMALL
#define	BABILE_SEL_BUFFERING7F			50|BUFFER_UNITACOUSTIC_ALL|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_SMALL|BUFFER_FORCE
#define	BABILE_SEL_BUFFERING5			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_ALL  |BUFFER_BERSTREAM_ALL
#define	BABILE_SEL_BUFFERING5F			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_ALL  |BUFFER_BERSTREAM_ALL  |BUFFER_FORCE
#define	BABILE_SEL_BUFFERING4			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_ALL
#define	BABILE_SEL_BUFFERING4F			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_ALL  |BUFFER_FORCE
#define	BABILE_SEL_BUFFERING3			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_SMALL
#define	BABILE_SEL_BUFFERING3F			50|BUFFER_UNITACOUSTIC_MED|BUFFER_UNITSOFFSETS_SMALL|BUFFER_BERSTREAM_SMALL|BUFFER_FORCE
#define BABILE_SEL_BUFFERING0			BABILE_SEL_BUFFERING3
#define BABILE_SEL_BUFFERING0F			BABILE_SEL_BUFFERING3F

#define BABILE_NLPMODULE_NULL		-1			/* Exclusive */
#define BABILE_NLPMODULE_NLPE		0			/* Exclusive */
#define BABILE_NLPMODULE_TTF		1			/* Exclusive */

#define BABILE_SYNTHMODULE_NULL			0		/* Can be used together */
#define BABILE_SYNTHMODULE_MBROLA		0x01	/* Can be used together */
#define BABILE_SYNTHMODULE_BBSELECTOR	0x02	/* Can be used together */
#define BABILE_SYNTHMODULE_COLIBRI		0x08	/* Can be used together */

#define BABILE_SYNTHACTIVE_MBROLA		0		/* Exclusive */
#define BABILE_SYNTHACTIVE_BBSELECTOR	0x0002		/* Exclusive */
#define BABILE_SYNTHACTIVE_NONE			0x0004		/* Exclusive */
#define BABILE_SYNTHACTIVE_COLIBRI		0x0008		/* Exclusive */
#define BABILE_SYNTHACTIVE_MASK			0x000E	
#define BABILE_NLPACTIVE_NLPE			0		/* Exclusive */
#define BABILE_NLPACTIVE_TTF			0x0001		/* Exclusive */
#define BABILE_NLPACTIVE_MASK			0x0001		

/*C# Wrapper:    public enum BABILE_SYNCENVENT : int { */
/*  BABILE callbacks types */
#define BABILE_SYNCPHOCALL		1			/* sync on phonemes */
#define BABILE_SYNCWORCALL		2			/* sync on words */
#define BABILE_SYNCBRECALL		3			/* sync on breath groups */
#define BABILE_SYNCSENCALL		4			/* sync on breath sentences */
#define BABILE_SYNCTXTCALL		5			/* sync on TEXT (start of text) */
#define BABILE_SYNCEOTCALL		6			/* sync on EOT (not used in BABILE)*/
#define BABILE_SYNCDURCALL		7			/* sync on ??? reserved for future use */
#define BABILE_SYNCDIPCALL		8			/* sync on diphones */
#define BABILE_SYNCSYLCALL		9			/* sync on syllables (not used in BABILE)*/
#define BABILE_SYNCNEWWINDOW	10			/* sync on analysis window update (compulsory) */
/*C# Wrapper: } BABILE_SYNCENVENT */


#endif  /* __BB_BABILE__IC_BABILE_H__ */
