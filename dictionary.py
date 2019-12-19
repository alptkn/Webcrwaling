def insert_dash(string,index,input):
	return string[:index] + input + string[index:]
	
 



Brand = {"asus"   : '%3Abrand%3A240',
		 "apple"  : '%3Abrand%3A230',
		 "lenovo" : '%3Abrand%3A2328',
		 "acer"   : '%3Abrand%3A204',
		 "hp"     : '%3Abrand%3A2267',
		 "casper" : '%3Abrand%3A290',
		 "dell"   : '%3Abrand%3A2152'}

Ram = {"4gb" : "%3ACLS-1047-RAM%3A4GB",
	   "8gb" : "%3ACLS-1047-RAM%3A8GB",
	   "16gb": "%3ACLS-1047-RAM%3A16GB"}


Processor = {"intel i5"     : "%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A8.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi5%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A10.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi5%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A5.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi5" , 
			 "intel i7"     : "%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A9.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi7%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A8.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi7%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A10.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi7",
			 "intel i3"     : "%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3A5.%2Bnesil%2BIntel%25C2%25AE%2BCore%25E2%2584%25A2%2Bi3",
			 "amd ryzen(5)" : "%3ACLS-1184-%C4%B0%C5%9Flemci+ailesi%3AAMD%2BRyzen%2B5"}


OS = {"Windows 10 Home" : "%3Aisletim-sistemi-yazilimi-cls-1095%3AWindows%2B10%2BHome%2B",
	  "Windows 10"      : "%3Aisletim-sistemi-yazilimi-cls-1095%3AWindows%2B10%2B",
	  "Macos-mojave"    : "%3Aisletim-sistemi-yazilimi-cls-1095%3AmacOS%2BMojave%2B",
	  "MacOS-Sierra"    : "%3Aisletim-sistemi-yazilimi-cls-1095%3AmacOS%2BSierra%2B"}



GPU = {"not include in"          :"%3ACLS-1163-Grafik%3AMevcut%2Bde%25C4%259Fil",
	   "NVIDIA GeForce MX230"    :"%3ACLS-1163-Grafik%3ANVIDIA%2BGeForce%2BMX2301",
	   "NVIDIA GeForce MX110"    :"%3ACLS-1163-Grafik%3ANVIDIA%25C2%25AE%2BGeForce%25C2%25AE%2BMX110",
	   "NVIDIA GeForce MX130"    :"%3ACLS-1163-Grafik%3ANVIDIA%25C2%25AE%2BGeForce%25C2%25AE%2BMX130",
	   "NVIDIA GeForce MX150"    :"%3ACLS-1163-Grafik%3ANVIDIA%25C2%25AE%2BGeForce%25C2%25AE%2BMX150",
	   "NVIDIA GeForce MX250"    :"%3ACLS-1163-Grafik%3ANVIDIA%25C2%25AE%2BGeForce%25C2%25AE%2BMX250",
	   "NVIDIA GeForce GTX1050"  :"%3ACLS-1163-Grafik%3ANVIDIA%25C2%25AE%2BGeForce%25C2%25AE%2BGTX%2B1050",
	   "AMD RadeonPro 555X"      :"%3ACLS-1163-Grafik%3AAMD%2BRadeon%2BPro%2B555X"}



HDD = {"SSD"       : "%3ACLS-1047-Depolama+ortam%C4%B1%3ASSD",
	   "HDD"       : "%3ACLS-1047-Depolama+ortam%C4%B1%3AHDD",
	   "HDD + SDD" : "%3ACLS-1047-Depolama+ortam%C4%B1%3AHDD%252BSSD"}



