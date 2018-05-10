import os

from webdemo import randomsentenceapp

if __name__ == '__main__':
    if 'DYNO' in os.environ:
        randomsentenceapp.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        randomsentenceapp.run(host='localhost', port=8080, debug=True)
