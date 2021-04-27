#!/usr/bin/env python
#Copyright (C) 2011 Robert Lanfear
#
#This program is free software: you can redistribute it and/or modify it
#under the terms of the GNU General Public License as published by the
#Free Software Foundation, either version 3 of the License, or (at your
#option) any later version.
#
#This program is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#General Public License for more details. You should have received a copy
#of the GNU General Public License along with this program.  If not, see
#<http://www.gnu.org/licenses/>.



# Genefinder is A script to search genbank for genes from a list of taxa
# This script can be used to put together large DNA datasets for any list of taxa and Genes.
# Note that the results should be checked by hand (e.g. by checking all alignments) since some sequences in GenBank will have misleading names.

# Citation: Lanfear, R. and Bromham, L, 2011. Estimating phylogenies for species assemblages: a complete phylogeny for the past and present native birds of New Zealand. Molecular Phylogenetics and Evolution, in press.

# Please note GenBank's rules of use, specifically this part: Run retrieval scripts on weekends or between 9 pm and 5 am Eastern Time weekdays for any series of more than 100 requests.


############# How to use the Script #############
# 1. Set the options below
# 2. On a mac, open Terminal and cd to the directory with the script in it, and type: "python GeneFinder.py"
# 3. An output file will be produced in the same directory as the script, which contains the longest Genank ID that matches any of the search terms, for each taxonID in the list


############## User options ########################
#define these before running the script
email_address = "" 				#enter your email address here, this is necessary for GenBank to keep track of script-users
retmax = 100 					#the maximum number of results you want from GenBank for each search. 100 is OK.
output_filename = "results.txt"	#this file will be created in the same directory as the script

#this is the list of terms that will be used to search GenBank. Change for each gene of interest.
search_terms = ["CYTB", "cytb", "cytochrome b", "Cytochrome b", "Cytochrome B", "cytochrome oxidase b", "Cytochrome Oxidase B"]

#this is the list of taxon IDs that will be searched in GenBank.
taxids = ["256038", "665151", "242120", "369484", "369483", "665152"]

####################################################

def search_all_GIs(taxid, searchterm, retmax):
	"""
	Get all GIs for a taxon ID, that match that ID, and the search term
	:param taxid: a genbank taxnomy ID as a string
	:param searchterm: a string, of 1 or more words
	N.B. Don't use spaces in the search term, use commas instead.	
	"""
	import urllib, re
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?&retmax=%d&term=txid%s[Organism:subtree]%s&' %(retmax, taxid, searchterm)
	params = {
		'db': 'nucleotide',
		'rettype': 'xml',
	}
	url = url + urllib.urlencode(params)
	data = urllib.urlopen(url).read()
	GIs = re.findall("<Id>(\S+)</Id>", data)
	return GIs

def get_summary(query, database, rettype):
	#Part of this function was taken from simon greenhill's work, with modification
	#here's an attribution to him:
	#!/usr/bin/env python
	# A short script to download nucleotide sequences from genbank.
	#
	# Copyright (c) 2009, Simon J. Greenhill <simon@simon.net.nz>
	# All rights reserved.
	#
	# Redistribution and use in source and binary forms, with or without
	# modification, are permitted provided that the following conditions
	# are met:
	#
	# 1. Redistributions of source code must retain the above copyright notice,
	#    this list of conditions and the following disclaimer.
	#
	# 2. Redistributions in binary form must reproduce the above copyright
	#    notice, this list of conditions and the following disclaimer in the
	#    documentation and/or other materials provided with the distribution.
	#
	# 3. Neither the name of genbank-download nor the names of its contributors
	#    may be used to endorse or promote products derived from this software
	#    without specific prior written permission.
	#
	# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
	# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
	# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
	# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
	# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
	# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
	# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
	# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
	# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
	# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
	# POSSIBILITY OF SUCH DAMAGE.
	import urllib
	_toolname = 'get_summary'
	_email = "enter_email_here"
	params = {
		'db': database,
		'tool': _toolname,
		'email': _email,
		'id': query,
		'rettype': rettype,
	}
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?'
	url = url + urllib.urlencode(params)
	data = urllib.urlopen(url).read()
	return data

def do_one_taxid(taxid, search_terms, retmax):
	import re
	import random
	from xml.dom import minidom
	import os
	import time

	#1. Get all GIs for that taxid
	GIs = []
	for name in search_terms:
		name = name.replace(" ", ",") #get rid of commas, since efetch doesn't like em. 
		temp = search_all_GIs(taxid, name, retmax)
		time.sleep(0.333) #don't overload genbank

		for thing in temp:
			GIs.append(str(thing))
	
	#2. Get the summaries of all the GIs
	GIdict = {}
	
	summary = get_summary(','.join(GIs), 'nucleotide', 'xml') #send in the big list of all GIs
	
	#now parse the GIs
	tempf = open("temp.xml", 'w')
	tempf.write(summary)
	tempf.close()
	
	xmldoc = minidom.parse("temp.xml")
	
	os.system("rm temp.xml")
	
	start = xmldoc.childNodes[1]
	nodelist = start.childNodes
	for thing in nodelist:
		if str(thing).count("DocSum")>0:
			GIsummary = thing.toxml()
			GI = str(int(re.search('<Item Name="Gi" Type="Integer">(\S+)</Item>', GIsummary).group(1)))
			GIdict[GI] = GIsummary
	
	#3. Throw out GIs whose name field doesn't match what you're looking for
	goodGIdict = {}
	for GI in GIdict:
		GIname = re.search('<Item Name="Title" Type="String">(.*)</Item>', GIdict[GI]).group(1)
		total_count = 0
		for thing in search_terms:
			total_count += GIname.count(thing)
		if total_count > 0: #if you didn't find any matches with the name you wanted
			goodGIdict[GI] = GIdict[GI]

	#4. pick the longest accession that's left
	longest = -999
	accessions = []
	lengthdict = {}

	if goodGIdict: #if there's anything left
		for GI in goodGIdict:
			length = int(str(re.search('<Item Name="Length" Type="Integer">(\S+)</Item>', goodGIdict[GI]).group(1)))
			lengthdict[length] = GI
		lengths = lengthdict.keys()
		lengths.sort()
		lengths.reverse()
		longest = lengths[0]
		longest_acc = lengthdict[longest]		

	else:
		longest_acc = 'x'
		
	#if you found>1 accession, randomly choose one
	if accessions:
		longest_acc = random.choice(accessions)
	
	return longest_acc


#this is the bit that actually does stuff
import time
outputfile = open(output_filename, 'w')
outputfile.write("taxid\tGID\n")
outputfile.close()
print "taxid\tGenbankGID"
for taxid in taxids:
	acc = do_one_taxid(str(taxid), search_terms, retmax)
	print "%s\t%s" %(taxid, acc),
	outputfile = open(output_filename, 'a')
	outputfile.write("%s\t%s\n" %(taxid, acc))
	outputfile.close()
	print "\n",
	time.sleep(0.333) #don't overload genbank
outputfile.close()