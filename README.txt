{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 INSTRUCTIONS:\
\
Type $python3 test.py  OR $python test.py\
\
Will be prompted to ENTER folder PATH where .txt files are located  i.e /Users/liamhan/Desktop/data \
(Important: do not include \'91 / \'91 at the end of file path location)\
\
\
\
Design: \
\
All .txt files located in a folder will be allocated into array D for each document i split into words.\
A temporary dictionary is used to aggregate all reoccurring terms for each word in D[i] .\
A new dictionary wordIndex is made where (key = term, value = [#doc, linked-list])). \
The linked-list holds the values for each posting as [docID, docFreq] }