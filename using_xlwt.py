# xlwt plugins 
import xlwt

wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet("my_sheet1")

for i in range(1, 10):
	for j in range(1, i+1):
		sheet1.write(i-1, j-1, "%s*%s = %s" % (j, i, j*i))

wbk.save("C:/test.xls")
print "Done!"