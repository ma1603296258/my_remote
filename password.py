'''
Author: your name
Date: 2021-09-10 11:25:28
LastEditTime: 2021-09-10 12:51:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \py\py\password.py
'''
import sys
import zipfile
import os
import threading
import time
import argparse
import itertools as its
from concurrent.futures import ThreadPoolExecutor


# �����ֵ�
a = "0123456789"  # ������
b = "abcdefghijklmnopqrstuvwxyz"  # ��Сд��ĸ
c = b.upper()  # ����д��ĸ
d = b+c  # ��Сд��ĸ���
e = a+d  # ����+��ĸ���


class BurpZip():
    def __init__(self, zipfile, file):
        self.file = zipfile
        self.Fpayload = file
        self.max_threads = 50                      # ����߳���
        self.exitflag = 1  # �ܿ���
        self.OpenFile()  # ��ѹ����

    def OpenFile(self):
        '''
        ��ѹ���������������Ϣ
        :return:
        '''
        file = open('E:\\���ϼ�\\2022����', 'r', encoding='gbk', errors='ignore')
       # self.file = open('E:\\���ϼ�\\2022������ѧ', 'r')
        if zipfile.is_zipfile(self.file):  # ����Ƿ�Ϊѹ����
            try:
                self.zp = zipfile.ZipFile(self.file)
                print("-"*35+"�ļ���Ϣ"+"-"*35+"\n")
                print(self.zp.printdir())  # ���ѹ�����ļ���Ϣ
                self.f = self.zp.namelist()[-1]  # ����Ϊ���һ���ļ���ȷ����Ŀ¼�����Ա��Ʋ���
                self.fatherpath = self.FilePath()
                print("-"*35+"�ļ���Ϣ"+"-"*35+"\n")
                self.Run()  # ��������
            except:
                print("���ִ���")
                sys.exit()
        else:
            print("warning�����ļ�����zipѹ����")
            sys.exit()

    def FilePath(self):
        '''
        ��ȡ�ļ���Ŀ¼·��
        :return: �ļ���Ŀ¼
        '''
        path = os.path.abspath(self.file)  # ��ȡ�ļ�����·��
        father_path = os.path.abspath(
            os.path.dirname(path) + os.path.sep + ".")  # ��ȡ��Ŀ¼
        return father_path

    def PayLoad(self, key, length):
        '''
        �������
        :param key: �����ֵ�
        :param length: ����ָ�����볤��
        :return:����
        '''

        payload = its.product(key, repeat=length)
        return payload

    def UnzipFileTest(self, pwd):
        '''
        ��ѹ���һ���ļ�
        :param pwd:��������
        :return: �ɹ����
        '''
        # fatherpath = self.FilePath()          #��ȡ�����ļ��ĸ�Ŀ¼

        try:
            self.zp.extract(self.f, path=self.fatherpath,
                            pwd=pwd.encode())  # ��ѹѹ����
            # print("ok")
            return pwd
        except:
            # print("no")
            return False

    def Run(self):
        '''
        ���ƽű�
        :return:
        '''
        # f = self.zp.namelist()[0]    #�Ȼ�ȡ��һ���ļ�
        res = self.UnzipFileTest(pwd="")
        if res != False:  # ���������Ƿ�Ϊ��
            print("[ ��ѹ����û���������� ]")  # ���п������
            sys.exit()
        else:
            print("***�ļ���ʧ�ܣ��ļ��������룬����������:***\n")
            pwd = input("���룺���������뱬����ֱ�ӻس���")
            if pwd != "":
                res = self.UnzipFileTest(pwd=pwd)
                if res:
                    print("[ ���룺{} ]".format(res))
                    sys.exit()
                else:
                    print("[ ���벻��ȷ��{} ]".format(str(pwd)))
            if self.Fpayload:
                payload = self.load_payloads()
                if payload:
                    print("[ payload����ɹ� ]")
                    self.TBURP(payload)
                else:
                    print("{}�ļ���ȡʧ��".format(self.Fpayload))
                    self.diy_payload()
            else:
                self.diy_payload()

    def diy_payload(self):
        '''
        �Զ���payload
        :return:
        '''
        key = input("��ѡ�񹥻��ֵ䣺a�����֣�b��Сд��ĸ��c����д��ĸ��d��Сд��ĸ��ϣ�e������ĸ��ϣ�Ĭ��e\n")
        length = input("������������볤������,Ĭ��8��\n")
        if key == "a":
            self.key = a
        if key == "b":
            self.key = b
        if key == "c":
            self.key = c
        if key == "d":
            self.key = d
        if key != "a" and key != "b" and key != "c" and key != "d":  # ���������ѡ����ֵ�
            self.key = e
        try:
            self.length = int(length)
        except:
            self.length = int("8")  # �������Ĭ�ϳ���Ϊ8
        print("��ʼ���ƣ�\n�����ֵ����ݣ�" + self.key + "\n���볤�����ޣ�" + str(self.length))
        self.ThreadRun()

    def load_payloads(self):
        '''
        ����payload
        :return:
        '''
        payloads = []
        F = open(self.Fpayload, 'r')
        for x in F:
            try:
                t = x.replace('\n', '')
                payloads.append(t)
            except:
                pass
        return payloads

    def Burp(self, key, length):
        '''
        ����PayLoad()��ʹ�����ɵ�������б���
        :param key: �����ֵ�
        :param length: ���볤��
        :return:
        '''

        Length = int(length)  # �������볤�ȣ����ٱ���ʱ��
        if(Length < 3):
            for x in self.PayLoad(key, length):  # ��������
                x = "".join(x)
                res = self.UnzipFileTest(pwd=x)
                if res:  # �����Խ�ѹ�ɹ������õ�ǰ�������ȫ����ѹ
                    print("[ ���룺{} ]".format(res))
                    sys.exit()
        else:
            if(Length % 2 == 1):
                RLength = Length/2  # �Ұ벿���볤��
                LLength = RLength+1  # ��벿���볤��
            else:
                LLength = Length/2
                RLength = LLength
            LLength = int(LLength)
            RLength = int(RLength)
            print("�߳�"+str(length) + "��" + str(LLength) + "+" + str(RLength))

            for L in self.PayLoad(key, LLength):
                for R in self.PayLoad(key, RLength):
                    L = "".join(L)
                    R = "".join(R)  # ����ת��
                    pwd = L+R
                    res = self.UnzipFileTest(pwd=pwd)
                    if res:
                        print("[ ���룺{} ]".format(res))
                        sys.exit()

            print("�߳�-" + str(length) + "��ֹͣ")
            return False  # �ж��߳�

    def TBURP(self, payload):
        '''
        ��������
        :param payload:
        :return:
        '''
        payload = payload
        with ThreadPoolExecutor(max_workers=500) as pool:
            results = pool.map(self.UnzipFileTest, payload)
        for result in results:
            if result:
                print("[ ���� ��{} ]".format(result))
                sys.exit()

    def ThreadRun(self):
        '''
        ÿ���߳����ض����ȵ�����
        :return:
        '''

        self.exitflag = 1
        threads = []
        for i in range(1, self.length+1):
            if self.exitflag == 1:
                thread = threading.Thread(
                    target=self.Burp, args=(self.key, i))  # ���������߳�
                threads.append(thread)  # ��ӽ��̳߳�
            else:
                threads = []  # self.exitflag==0ʱ ����̳߳�
        for t in threads:
            t.start()
        while 1:
            time.sleep(0.05)  # ��ֹ�̶߳���

    def FileClose(self):
        '''
        �ر��ļ�
        :return:
        '''
        self.zp.close()


def main():
    ter_opt = {}
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    parser = argparse.ArgumentParser(
        description='����ZIPѹ�������뱬�ƹ���', add_help=True)
    parser.add_argument('-f', '--file', help='��Ҫ���Ƶ�ѹ�����ļ�')
    parser.add_argument('-e', default=None, help='�Զ�����ⲿ���뱾')
    args = parser.parse_args()
    for opt, val in args._get_kwargs():
        ter_opt[opt] = val
    if not ter_opt['file']:
        sys.exit(1)
    else:
        R = BurpZip(ter_opt['file'], ter_opt['e'])
    print("[ û�б��Ƴ���ȷ���� ]")


if __name__ == "__main__":
    main()
