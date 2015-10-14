import unittest

from taipan.T2D.Sampler import T2DSampler
from taipan.T2D.Table import T2DTable
from taipan.Learning.SubjectColumnIdentification.SimpleIdentifier import SimpleIdentifier
from taipan.Learning.SubjectColumnIdentification.DistantSupervisionIdentifier import DistantSupervisionIdentifier

from taipan.Logging.Logger import Logger

# class SimpleIdentifierBenchTestCase(unittest.TestCase):
#     def setUp(self):
#         sampler = T2DSampler()
#         self.testTable = sampler.getTestTable()
#         self.simpleIdentifier = SimpleIdentifier()

    # def testSimpleColumnIdentifierOne(self):
    #     colNumber = self.simpleIdentifier.identifySubjectColumn(self.testTable)
    #     self.assertTrue(self.testTable.isSubjectColumn(colNumber), msg="colNumber should be subject column")

class SubjectColumnIdentificationBenchTestCase(unittest.TestCase):
    def setUp(self):
        sampler = T2DSampler()
        self.testTable = sampler.getTestTable()
        self.dlIdentifier = DistantSupervisionIdentifier()
        self.simpleIdentifier = SimpleIdentifier()
        #self.testTables20 = sampler.get20Tables()
        #self.testTables = sampler.getTablesSubjectIdentification()

    def resultsPrinter(self, results, filename):
        import csv
        import os
        filename = os.path.join("results",filename)
        with open(filename, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for result in results:
                spamwriter.writerow(result)

    def distantLearningIdentifier(self, rowsToAnalyze, tables, resultsFilename):
        results = [["tableId","rowsToAnalyze","tableSize","subjectColumnIdx","identifiedCorrectly","executionTimeFull","executionTimePure","queryTime","disambiguationTime"]]
        for table in tables:
            colNumber = self.dlIdentifier.identifySubjectColumn(table)
            identifiedCorrectly = table.isSubjectColumn(colNumber)
            tableSize = len(table.getData())
            result = [table.id, rowsToAnalyze, tableSize, colNumber, identifiedCorrectly, self.dlIdentifier.executionTimeFull, self.dlIdentifier.executionTimePure, self.dlIdentifier.queryTime, self.dlIdentifier.agdistisTime]
            results.append(result)
        self.resultsPrinter(results, resultsFilename)

    def testDistantLearningIdentifierOne(self):
        self.distantLearningIdentifier(20, [self.testTable], "testOneTable.20rows.csv")

    def testDistantLearningIdentifierTwenty(self):
        self.distantLearningIdentifier(20, self.testTables20, "test20tables.20rows.csv")

    def testDistantLearningIdentifierAll(self):
        """
            With 1 row only!

            Tables analyzed: 900
            Subject Column Identified Correctly: 762
            Precision: 0.846666666667

            Tables analyzed: 1687
            Subject Column Identified Correctly: 1461
            Precision: 0.866034380557
        """
        self.testDistantLearningIdentifier(20, self.testTables, "testAlltables.20rows.csv")

    # def testSimpleColumnIdentifierAll(self):
    #     """
    #         Tables analyzed: 900
    #         Subject Column Identified Correctly: 893
    #         Precision: 0.992222222222
    #     """
    #     overall = 900
    #     correct = 0
    #     for table in self.testTables[:900]:
    #         colNumber = self.simpleIdentifier.identifySubjectColumn(self.testTable)
    #         if(table.isSubjectColumn(colNumber)):
    #             correct += 1
    #     precision = float(correct)/overall
    #     print "Tables analyzed: %s\nSubject Column Identified Correctly: %s\nPrecision: %s" % (overall, correct, precision,)
?
    # def testDistantLearningIdentifierProblematic(self):
    #     tableId = "65842312_0_4733067625464702086.csv" #Got ???? symbols in the cells
    #     tableId = "95942871_9_1442908185816138298.csv" #utf-8 can not encode char
    #     table = T2DTable(tableId)
    #     colNumber = self.dlIdentifier.identifySubjectColumn(table)
