from . import formula

def from_gregorian(y, m, d):
	# valid from 1420 AH (1999-04-17 CE) to 1450 AH (2029-05-14 CE)
	jd = int(formula.gregorian_to_jd(y, m, d) + 0.5) # jd midday
	accu = 2451286 # jd of 1999-04-17 midday
	i = -1
	while accu <= jd:
		i += 1
		accu += _month_len[i] + 29
	if i == -1: raise IndexError(i)
	month_start = accu - _month_len[i] - 29
	# here i is index where the month we're looking for is
	h_year = i // 12 + 1420
	h_month = i % 12 + 1
	h_day = jd - month_start + 1
	return (h_year, h_month, h_day, formula.jd_to_weekday(jd), _month_len[i])

def to_gregorian(y, m, d):
	index = (y - 1420) * 12 + m - 1
	if index < 0 or index > len(_month_len): raise IndexError(index)
	jd = 2451285.5 + sum(i + 29 for i in _month_len[:index]) + d - 1
	return formula.jd_to_gregorian(jd)

_month_len = (0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 
	0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 
	1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 
	1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 
	1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 
	1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 
	0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 
	0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 
	1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 
	0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 
	0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 
	0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 
	0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 
	1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 
	0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 
	1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 
	0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 
	1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 
	1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 
	1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 
	0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 
	1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 
	0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 
	1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 
	0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 
	0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 
	0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 
	1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 
	0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 
	0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 
	1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1)

