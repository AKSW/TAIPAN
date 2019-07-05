default:
	echo "no default target for this make file"
	echo "to run test: make test"

install: requirements
	cp taipan/Config/ExternalUris.py-sample taipan/Config/ExternalUris.py

test:
	python -m unittest discover -s ./taipan/Tests -p "*Test.py"

test-subject-column-support-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification -p "SupportIdentifierTest.py"

test-subject-column-supervised-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification/Supervised -p "SupervisedIdentifierTest.py"

test-subject-column-support-connectivity-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification -p "SupportConnectivityIdentifierTest.py"

test-subject-column-connectivity-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification -p "ConnectivityIdentifierTest.py"

test-subject-column-simple-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification -p "SimpleIdentifierTest.py"

test-t2d-sampler:
	python -m unittest discover -s ./taipan/Tests/T2D -p "SamplerTest.py"

test-simple-cache-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyMapping -p "SimpleCachePropertyMappingTest.py"

test-simple-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyMapping -p "SimplePropertyMappingTest.py"

test-lov-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyMapping -p "LovPropertyMappingTest.py"

test-ranked-lov-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyMapping -p "RankedLovPropertyMappingTest.py"

test-t2k-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyMapping -p "T2KPropertyMappingTest.py"

test-distant-supervision-identifier:
	python -m unittest discover -s ./taipan/Tests/Learning/SubjectColumnIdentification -p "DistantSupervisionIdentifierTest.py"

test-simple-property-recommender:
	python -m unittest discover -s ./taipan/Tests/Learning/PropertyRecommendation -p "SimplePropertyRecommenderTest.py"

benchmark:
	python -m unittest discover -s ./taipan/Tests -p "*Bench.py"

benchmark-subject-column-identification:
	python -m unittest discover -s ./taipan/Tests/Benchmarking -p "SubjectColumnIdentificationBench.py"

benchmark-simple-cache-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Benchmarking -p "SimpleCachePropertyMappingBench.py"

benchmark-simple-property-mapping:
	python -m unittest discover -s ./taipan/Tests/Benchmarking -p "SimplePropertyMappingBench.py"

clean-windows-characters:
	bash scripts/cleanWindowsCharacters.sh

requirements:
	pip install -r requirements.txt

requirements-server:
	pip install flask
	pip install flask-wtf
	pip install oauth2client
	pip install PyOpenSSL
	pip install pymongo

get-properties-for-table:
	python scripts/getPropertiesForTable.py ${ARGS}
