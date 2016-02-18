import netCDF4 as netCDF
from extraction_utils import basic, getCsvDict
import json

class TransectStats(object):
	"""docstring for TransectStats"""
	def __init__(self, filename, variable, _csv):
		super(TransectStats, self).__init__()
		self.filename = filename
		self.variable = variable
		self._csv = _csv
		

	def process(self):
		print "running basic processing on %s" % self.filename
		data = getCsvDict(self._csv)
		for row in data:
			print "getting data from %f %f for %s" % (row['Lat'], row['Lon'], row['Date'])
		netcdf_file = netCDF.Dataset(self.filename, "r")
		return data


		#netcdf_variable = netcdf_file[variable]





		