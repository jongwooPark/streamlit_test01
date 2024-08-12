import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import streamlit.components.v1 as components
from dotenv import load_dotenv
from openai import OpenAI


def app():
    st.title("엄이디퓨전 라이브러리")
    st.subheader("엄이디퓨전 아이템을 활용하세요.")

    item = {
        "name" : "프로젝트",
        "types" : ["물", "땅"],
        "image_url" : ""
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander(label="프로젝트a", expanded=True):
            st.image("./images/00001-2307861541.png")
            st.write(f"모델명:architectureInterior_v70")
        # 클립보드 복사 버튼 생성
        # Custom HTML/JS Component
            text_to_copy ="""
((A photography showcase of Fallingwater, the iconic architecture by Frank Lloyd Wright located in Mill Run, Pennsylvania. Through the lens of Ansel Adams, using a 35mm lens, the scene captures the house’s unique cantilevered terraces amidst the verdant forest. The color temperature exudes a cool blueish tint. No facial expressions as the primary focus is on the structure. Ambient light from the sun provides a gentle glow to the scene, casting soft shadows. The atmosphere is serene and timeless))
Dive into the world of Photography that captures the essence of Frank Lloyd Wright's modern 
Frank Lloyd Wright's modern style villa with a focus on the architectural marvel of Fallingwater. Through a 35mm lens, witness the structure in intense clarity and sharpness. The image has a warm color temperature that highlights the building's iconic cascading forms. No facial expressions are present as the image focuses solely on architecture. The lighting is natural, with the sun casting soft shadows on the structure, giving depth and texture. The atmosphere feels serene and untouched by time
Steps: 50, Sampler: Euler a, CFG scale: 7, Seed: 4056340336, Size: 768x768, Model hash: 03b2d23370, Model: architectureExterior_v40Exterior, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, Version: 1.7.0
""".replace("\n", "").replace('"', '\\"')

            components.html(f"""
                <style>
                    .streamlit-button {{
                        background-color: rgb(255 255 255);
                        color: black;
                        padding: 0.5rem 0.75rem;
                        border-radius: 0.5rem;
                        border: 1px solid #c3c3c3;
                        cursor: pointer;
                        font-size: 16px;
                        font-family: "Source Sans Pro", sans-serif;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        margin-top: 0.5rem;
                        margin-bottom: 0.5rem;
                    }}
                    .streamlit-button:hover {{
                        background-color: rgb(255 255 255);
                        border: 1px solid #ff0000;
                        color: #e02f2f;
                    }}
                </style>
                <button class="streamlit-button" onclick="copyToClipboard()">복사</button>
                <script>
                    function copyToClipboard() {{
                        setTimeout(function() {{
                            navigator.clipboard.writeText("{text_to_copy}").then(function() {{
                                alert('엄이디퓨전 정보가 복사되었습니다.');
                            }}, function(err) {{
                                console.error('복사 중 오류 발생:', err);
                            }});
                        }}, 100); // 100ms 딜레이를 주어 UI가 먼저 렌더링되도록 함
                    }}
                </script>
            """, height=100)
            
           

    with col2:
        with st.expander(label="프로젝트2", expanded=True):
            st.image("./images/00005-4056340336.png")
            st.write(f"모델명:architectureExterior_v40Exterior")
        # 클립보드 복사 버튼 생성
        # Custom HTML/JS Component
            text_to_copy = """
((A photography showcase of Fallingwater, the iconic architecture by Frank Lloyd Wright located in Mill Run, Pennsylvania. Through the lens of Ansel Adams, using a 35mm lens, the scene captures the house’s unique cantilevered terraces amidst the verdant forest. The color temperature exudes a cool blueish tint. No facial expressions as the primary focus is on the structure. Ambient light from the sun provides a gentle glow to the scene, casting soft shadows. The atmosphere is serene and timeless))
Dive into the world of Photography that captures the essence of Frank Lloyd Wright's modern "Frank Lloyd Wright's modern style villa" with a focus on the architectural marvel of Fallingwater. Through a 35mm lens, witness the structure in intense clarity and sharpness. The image has a warm color temperature that highlights the building's iconic cascading forms. No facial expressions are present as the image focuses solely on architecture. The lighting is natural, with the sun casting soft shadows on the structure, giving depth and texture. The atmosphere feels serene and untouched by time
A modern house seamlessly integrates natural elements into its design. featuring a balcony adorned with lush greenery and a front yard that blends nature with the environment. Soft ambient lighting casts a warm and welcoming glow. Channeling the spirit of renowned architect Frank Lloyd Wright, this design showcases his signature organic architectural style. The medium for this artwork is an architectural blueprint rendered in high-definition 3D graphics, emphasizing every detail of the design. The color scheme mainly consists of earthy tones and various shades of green, enhancing the connection to nature
Negative prompt: ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, Body out of frame, Blurry, Bad art, Bad anatomy, Blurred, Watermark, Grainy, Duplicate
Steps: 50, Sampler: Euler a, CFG scale: 7, Seed: 4056340336, Size: 768x768, Model hash: 03b2d23370, Model: architectureExterior_v40Exterior, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, Version: 1.7.0
                 """.replace("\n", "").replace('"', '\\"')

            components.html(f"""
                <style>
                    .streamlit-button {{
                        background-color: rgb(255 255 255);
                        color: black;
                        padding: 0.5rem 0.75rem;
                        border-radius: 0.5rem;
                        border: 1px solid #c3c3c3;
                        cursor: pointer;
                        font-size: 16px;
                        font-family: "Source Sans Pro", sans-serif;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        margin-top: 0.5rem;
                        margin-bottom: 0.5rem;
                    }}
                    .streamlit-button:hover {{
                        background-color: rgb(255 255 255);
                        border: 1px solid #ff0000;
                        color: #e02f2f;
                    }}
                </style>
                <button class="streamlit-button" onclick="copyToClipboard()">복사</button>
                <script>
                    function copyToClipboard() {{
                        setTimeout(function() {{
                            navigator.clipboard.writeText("{text_to_copy}").then(function() {{
                                alert('엄이디퓨전 정보가 복사되었습니다.');
                            }}, function(err) {{
                                console.error('복사 중 오류 발생:', err);
                            }});
                        }}, 100); // 100ms 딜레이를 주어 UI가 먼저 렌더링되도록 함
                    }}
                </script>
            """, height=100)




    with col3:
        with st.expander(label="프로젝트2", expanded=True):
            st.image("./images/00009-809968412.png")
            st.write(f"모델명:architectureExterior_v40Exterior")
        # 클립보드 복사 버튼 생성
        # Custom HTML/JS Component
            text_to_copy = """
A futuristic and stunningly beautiful high-rise shopping center architectural structure with bold, futuristic design elements, blending seamlessly into the art form of digital illustration. Inspired by the works of Syd Mead. The scene showcases the center amidst a bustling city, its sleek lines contrasting with the urban environment. A warm color temperature adds vibrancy, highlighting the architectural details. Shoppers and visitors exhibit expressions of awe and excitement. Illuminated by soft, diffused lighting, the atmosphere exudes sophistication and promise of tomorrow
(masterpiece),(high quality), best quality, real,(realistic), super detailed, (full detail),(4k),8k,no humans, scenery, building, ((500-meter tall buildings)),outdoors, window, road, sky, street, lamppost, tree, power lines,,Organic modernist architecture, glass curtain walls, interesting shapes, super high-rise buildings in the block
Negative prompt: (normal quality), (low quality), (worst quality), paintings, sketches,fog,signature,soft, blurry,drawing,sketch, poor quality, uply text,type, word, logo, pixelated, low resolution.,saturated,high contrast, oversharpened,dirt
Steps: 50, Sampler: Euler a, CFG scale: 7.5, Seed: 809968412, Size: 512x768, Model hash: 03b2d23370, Model: architectureExterior_v40Exterior, Denoising strength: 0.7, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires steps: 18, Hires upscaler: 4x-UltraSharp, Version: 1.7.0
                 """.replace("\n", "").replace('"', '\\"')

            components.html(f"""
                <style>
                    .streamlit-button {{
                        background-color: rgb(255 255 255);
                        color: black;
                        padding: 0.5rem 0.75rem;
                        border-radius: 0.5rem;
                        border: 1px solid #c3c3c3;
                        cursor: pointer;
                        font-size: 16px;
                        font-family: "Source Sans Pro", sans-serif;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        margin-top: 0.5rem;
                        margin-bottom: 0.5rem;
                    }}
                    .streamlit-button:hover {{
                        background-color: rgb(255 255 255);
                        border: 1px solid #ff0000;
                        color: #e02f2f;
                    }}
                </style>
                <button class="streamlit-button" onclick="copyToClipboard()">복사</button>
                <script>
                    function copyToClipboard() {{
                        setTimeout(function() {{
                            navigator.clipboard.writeText("{text_to_copy}").then(function() {{
                                alert('엄이디퓨전 정보가 복사되었습니다.');
                            }}, function(err) {{
                                console.error('복사 중 오류 발생:', err);
                            }});
                        }}, 100); // 100ms 딜레이를 주어 UI가 먼저 렌더링되도록 함
                    }}
                </script>
            """, height=100)             

         

        
