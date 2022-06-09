echo "======== %%%%%%%%%%  FILE TXT  %%%%%%%%%% ========="
echo "======== REQUEST ((((50)))) CONCURRENCY 10 FILE TXT ========="
ab -n 50 -c 10 http://172.16.16.101:8889/testing.txt 

echo "======== REQUEST ((((100)))) CONCURRENCY 10 FILE TXT ========"
ab -n 100 -c 10 http://172.16.16.101:8889/testing.txt

echo "======== REQUEST ((((200)))) CONCURRENCY 10 FILE TXT ========"
ab -n 200 -c 10 http://172.16.16.101:8889/testing.txt

echo "======== REQUEST ((((300)))) CONCURRENCY 10 FILE TXT ========"
ab -n 300 -c 10 http://172.16.16.101:8889/testing.txt

echo "======== REQUEST ((((500)))) CONCURRENCY 10 FILE TXT ========"
ab -n 500 -c 10 http://172.16.16.101:8889/testing.txt

echo "======== REQUEST ((((1000)))) CONCURRENCY 10 FILE TXT ========"
ab -n 1000 -c 10 http://172.16.16.101:8889/testing.txt

echo "======== REQUEST ((((10000)))) CONCURRENCY 10 FILE TXT ========"
ab -n 10000 -c 10 http://172.16.16.101:8889/testing.txt

echo "[][][][][][] SERVER TEST WITH TXT EXTENSION DONE [][][][][][]"

echo "======== %%%%%%%%%%  FILE PDF  %%%%%%%%%% ========="
echo "======== REQUEST ((((50)))) CONCURRENCY 10 FILE PDF ========="
ab -n 50 -c 10 http://172.16.16.101:8889/rfc2616.pdf 

echo "======== REQUEST ((((100)))) CONCURRENCY 10 FILE PDF ========"
ab -n 100 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "======== REQUEST ((((200)))) CONCURRENCY 10 FILE PDF ========"
ab -n 200 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "======== REQUEST ((((300)))) CONCURRENCY 10 FILE PDF ========"
ab -n 300 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "======== REQUEST ((((500)))) CONCURRENCY 10 FILE PDF ========"
ab -n 500 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "======== REQUEST ((((1000)))) CONCURRENCY 10 FILE PDF ========"
ab -n 1000 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "======== REQUEST ((((10000)))) CONCURRENCY 10 FILE PDF ========"
ab -n 10000 -c 10 http://172.16.16.101:8889/rfc2616.pdf

echo "[][][][][][] SERVER TEST WITH PDF EXTENSION DONE [][][][][][]"

echo "======== %%%%%%%%%%  FILE JPG  %%%%%%%%%% ========="
echo "======== REQUEST ((((50)))) CONCURRENCY 10 FILE JPG ========="
ab -n 50 -c 10 http://172.16.16.101:8889/pokijan.jpg 

echo "======== REQUEST ((((100)))) CONCURRENCY 10 FILE JPG ========"
ab -n 100 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "======== REQUEST ((((200)))) CONCURRENCY 10 FILE JPG ========"
ab -n 200 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "======== REQUEST ((((300)))) CONCURRENCY 10 FILE JPG ========"
ab -n 300 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "======== REQUEST ((((500)))) CONCURRENCY 10 FILE JPG ========"
ab -n 500 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "======== REQUEST ((((1000)))) CONCURRENCY 10 FILE JPG ========"
ab -n 1000 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "======== REQUEST ((((10000)))) CONCURRENCY 10 FILE JPG ========"
ab -n 10000 -c 10 http://172.16.16.101:8889/pokijan.jpg

echo "[][][][][][] SERVER TEST WITH JPG EXTENSION DONE [][][][][][]"