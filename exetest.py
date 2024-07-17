from datetime import datetime
        
from flask import Flask, render_template,request,url_for
import json
import os
import random
import glob

            
page =[]


app = Flask(__name__)

@app.route('/')
def mofr():
    basetxta =""

    basetxta+="""<!DOCTYPE html>
    <html>
    <body>

    <!-- 画像を重ねて配置 --><div style="position: relative;">               """
    imgs =glob.glob(r"static\images\*.png")
    imgs +=glob.glob(r"static\images\*.jpg")
    print(imgs)
    for i in imgs:
#        f'<img id="image1" src="img1.jpg" style="position: absolute; top: 0; left: 0;">'
        basetxta+='<img id="image3" src="' +url_for('static', filename=i.replace('\\', '/').replace('//', '/').replace('static', ''))+'" alt="Example Image" style="position: absolute; top: 0; left: 0;">'
    basetxta +="""  
    <!-- 他の画像も同様に追加 -->
    </div>

    <script>
    // すべての画像を取得
    var images = document.getElementsByTagName('img');

    // 最初の画像以外を非表示にする
    for (var i = 1; i < images.length; i++) {
    images[i].style.display = 'none';
    }

    // 現在表示している画像のインデックス
    var currentImageIndex = 0;

    // 'pause'キーが押されたときの処理
    document.addEventListener('keydown', function(event) {
    if (event.key === 'Pause') {  // 'pause'キーが押された場合
    // 現在の画像を非表示にする
    images[currentImageIndex].style.display = 'none';

    // 次の画像のインデックスを計算（ループする）
    currentImageIndex = (currentImageIndex + 1) % images.length;

    // 次の画像を表示する
    images[currentImageIndex].style.display = 'block';
    }
    });
    </script>

    </body>
    </html>
    """
    
    
    return basetxta
        









if __name__ == '__main__':
    app.run(debug=True)
