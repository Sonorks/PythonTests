#!/usr/bin/env python
# -*- coding: utf-8 -*-




def convertir(decimal):
    
    if decimal > 100 or decimal == 0: 
        raise UnboundLocalError('El numero debe estar entre 1 y 100')
    if decimal == 100 : return 'C'
    romano_dec = decimal % 100 // 10
    romano_un = decimal % 100 % 10 
    dec_d = {1:'X',2:'XX',3:'XXX',4:'XL',5:'L',\
        6:'LX',7:'LXX',8:'LXXX',9:'XC'}
    dec_u = {1:'I',2:'II',3:'III',4:'IV',5:'V',\
        6:'VI',7:'VII',8:'VIII',9:'IX'}
    romano = ''
    if romano_dec: romano += dec_d[romano_dec]
    if romano_un: romano += dec_u[romano_un]
    
    return romano
    