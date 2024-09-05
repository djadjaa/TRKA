import matplotlib.pyplot as plt


F = 400  
m = 80   


a = F / m  


plt.figure(figsize=(6, 3))
plt.title('Diagram sprintera')


plt.arrow(0, 0, F/100, 0, head_width=0.1, head_length=20, fc='blue', ec='blue', label='Vucna sila')


otpor_vazduha = F * 0.1
plt.arrow(F/100, 0, -otpor_vazduha/100, 0, head_width=0.1, head_length=20, fc='red', ec='red', label='Otpor vazduha')


plt.text(F/100 + 10, 0.05, '400 N', color='blue')
plt.text(F/100 - otpor_vazduha/100 - 60, 0.05, f'{otpor_vazduha:.0f} N', color='red')

plt.xlim(-50, 450)
plt.ylim(-1, 1)
plt.gca().axes.get_yaxis().set_visible(False)
plt.axhline(0, color='black')  
plt.show()
