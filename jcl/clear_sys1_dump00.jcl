//CDUMP JOB (TSO),'CDUMP',
//         CLASS=A,
//         MSGCLASS=A,
//         MSGLEVEL=(1,1),
//         USER=IBMUSER,PASSWORD=SYS1,
//         REGION=8192K,
//         NOTIFY=HMVS01
//CP01   EXEC PGM=IEBGENER
//SYSUT1    DD DUMMY
//SYSUT2    DD DSN=SYS1.DUMP00,DISP=OLD
//SYSPRINT  DD SYSOUT=*
//SYSOUT    DD SYSOUT=*
//SYSIN     DD *
/* ------------------------------------------