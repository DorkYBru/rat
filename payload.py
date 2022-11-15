from cryptography.fernet import Fernet
f= Fernet("""owKN-~GF}ODo.{Yn"G5bzBzBuL`Wa06l5(Z-EQG8G,J~/0H;u2twpfb9U'_P%w2tX[Gg%luDu#:8`I,i|vob3X@o[nvLU4dq9TaR$@T0U,oVF}q(;u208FvfMz:`FZHq""")
script=""" """
decrypt_script= f.decrypt(script)