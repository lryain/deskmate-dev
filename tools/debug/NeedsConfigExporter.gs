// Cozmo needs system configuration data exporter


// Includes functions for exporting active sheet or all sheets as JSON object (also Python object syntax compatible).
// Tweak the makePrettyJSON_ function to customize what kind of JSON to export.

var FORMAT_ONELINE   = 'One-line';
var FORMAT_MULTILINE = 'Multi-line';
var FORMAT_PRETTY    = 'Pretty';

var LANGUAGE_JS      = 'JavaScript';
var LANGUAGE_PYTHON  = 'Python';

var STRUCTURE_LIST = 'List';
var STRUCTURE_HASH = 'Hash (keyed by "id" column)';

/* Defaults for this particular spreadsheet, change as desired */
var DEFAULT_FORMAT = FORMAT_PRETTY;
var DEFAULT_LANGUAGE = LANGUAGE_JS;
var DEFAULT_STRUCTURE = STRUCTURE_LIST;


function comment(sheetName) {
  var comment = "// Do not edit this file manually.\n// This file was exported from the Google sheet at https://docs.google.com/spreadsheets/d/1DivDR3KR0gH5D_34jBZKdGJFwqXRjAQE9TvCWgtkVKM/edit#gid=1435598582\n";
  comment += "// (Sheet name: \"" + sheetName + "\")\n";
  var now = new Date();
  comment += "// Exported on " + (now.getMonth() + 1) + "/" + now.getDate() + "/" + now.getFullYear();
  var mins = now.getMinutes();
  comment += " at " + now.getHours() + ":";
  if (mins < 10) {
    comment += '0';
  }
  comment += mins + "\n\n";
  return comment;
}

function onOpen() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var menuEntries = [
    {name: "Export JSON for MainConfig sheet", functionName: "exportMainConfigSheet"},
//    {name: "Export JSON for MainConfigA sheet", functionName: "exportMainConfigASheet"},
//    {name: "Export JSON for MainConfigB sheet", functionName: "exportMainConfigBSheet"},
//    {name: "Export JSON for MainConfigC sheet", functionName: "exportMainConfigCSheet"},
//    {name: "Export JSON for MainConfigD sheet", functionName: "exportMainConfigDSheet"},
    {name: "Export JSON for ActionConfig sheet", functionName: "exportActionConfigSheet"},
//    {name: "Export JSON for ActionConfigOrig sheet", functionName: "exportActionConfigOrigSheet"},
    {name: "Export JSON for DecayConfig sheet", functionName: "exportDecayConfigSheet"},
    {name: "Export JSON for RewardsConfig sheet", functionName: "exportRewardsConfigSheet"},
//    {name: "Export JSON for RewardsConfigOrig sheet", functionName: "exportRewardsConfigOrigSheet"},
    {name: "Export JSON for LocalNotificationConfig sheet", functionName: "exportLocalNotificationConfigSheet"},
//  {name: "Configure export", functionName: "exportOptions"},
  ];
  ss.addMenu("Export JSON", menuEntries);
}

function makeTextBox(app, name) { 
  var textArea = app.createTextArea().setWidth('100%').setHeight('200px').setId(name).setName(name);
  return textArea;
}

/*
function exportAllSheets(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  var sheetsData = {};
  for (var i = 0; i < sheets.length; i++) {
    var sheet = sheets[i];
    var rowsData = getRowsData_(sheet, getExportOptions(e));
    var sheetName = sheet.getName(); 
    sheetsData[sheetName] = rowsData;
  }
  var json = makeJSON_(sheetsData, getExportOptions(e));
  return displayText_(json);
}
*/

function exportMainConfigSheet(e) {
  var sheetName = "MainConfig";
  var rowsData = GetRowsFromMainConfig(sheetName);
  var json = makeJSON_(rowsData, getExportOptions(e));
  json = comment(sheetName) + json + '\n';
  return displayText_(json);
}

function GetRowsFromMainConfig(sheetName) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var rowsData = getRowsOfKVPs_(sheet);
  return rowsData;
}

function exportMainConfigASheet(e) {
  return exportMainConfigDeltaSheet(e, "MainConfigA");
}

function exportMainConfigBSheet(e) {
  return exportMainConfigDeltaSheet(e, "MainConfigB");
}

function exportMainConfigCSheet(e) {
  return exportMainConfigDeltaSheet(e, "MainConfigC");
}

function exportMainConfigDSheet(e) {
  return exportMainConfigDeltaSheet(e, "MainConfigD");
}

function exportMainConfigDeltaSheet(e, sheetName) {
  // First, read the default sheet rows
  var rowsData = GetRowsFromMainConfig("MainConfig");

  // Now, read the rows from the 'delta' sheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var deltaRowsData = getRowsOfKVPs_(sheet);

  // Overlay the delta data onto the default data
  for (var key in deltaRowsData) {
    rowsData[key] = deltaRowsData[key];
  }

  var json = makeJSON_(rowsData, getExportOptions(e));
  json = comment(sheetName) + json + '\n';
  return displayText_(json);
}

function exportActionConfigSheet(e) {
  return exportActionConfigSheetInternal(e, "ActionConfig");
}

function exportActionConfigOrigSheet(e) {
  return exportActionConfigSheetInternal(e, "ActionConfigOrig");
}

function exportActionConfigSheetInternal(e, sheetName) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var rowsData = getRowsData_(sheet);
  // Error-checking:  Ensure 'range' columns are non-negative:
  for (var i = 0; i < rowsData.length; i++) {
    if (rowsData[i]["repairRange"] < 0) {
      return displayText_(rangeError(rowsData[i]["actionId"], "repairRange"));
    }
    if (rowsData[i]["energyRange"] < 0) {
      return displayText_(rangeError(rowsData[i]["actionId"], "energyRange"));
    }
    if (rowsData[i]["playRange"] < 0) {
      return displayText_(rangeError(rowsData[i]["actionId"], "playRange"));
    }
  }
  var json = makeJSON_(rowsData, getExportOptions(e));
  json = comment(sheetName) + '{ "actionDeltas":' + json + ' }\n';
  return displayText_(json);
}

function rangeError(actionIdName, fieldName) {
  return "Error: For actionId " + actionIdName + ", " + fieldName + " cannot be negative.";
}

function exportDecayConfigSheet(e) {
  return exportGivenDecayConfigSheet(e, "DecayConfig");
}

function exportGivenDecayConfigSheet(e, sheetName) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var data = getDecayData_(sheet);
  var json = makeJSON_(data, getExportOptions(e));
  json = comment(sheetName) + json + '\n';
  return displayText_(json);
}

function exportRewardsConfigSheet(e) {
  return exportRewardsConfigSheetInternal(e, "RewardsConfig");
}

function exportRewardsConfigOrigSheet(e) {
  return exportRewardsConfigSheetInternal(e, "RewardsConfigOrig");
}

function exportRewardsConfigSheetInternal(e, sheetName) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var data = getRewardsData_(sheet);
  var json = makeJSON_(data, getExportOptions(e));
  json = comment(sheetName) + json + '\n';
  return displayText_(json);
}

function exportLocalNotificationConfigSheet(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheetName = "LocalNotificationConfig";
  var sheet = ss.getSheetByName(sheetName);
  var data = getLocalNotificationData_(sheet);
  var json = makeJSON_(data, getExportOptions(e));
  json = comment(sheetName) + json + '\n';
  return displayText_(json);
}

function getExportOptions(e) {
  var options = {};
  
  options.language = e && e.parameter.language || DEFAULT_LANGUAGE;
  options.format   = e && e.parameter.format || DEFAULT_FORMAT;
  options.structure = e && e.parameter.structure || DEFAULT_STRUCTURE;
  
  var cache = CacheService.getPublicCache();
  cache.put('language', options.language);
  cache.put('format',   options.format);
  cache.put('structure', options.structure);
  
  Logger.log(options);
  return options;
}

function makeJSON_(object, options) {
  if (options.format == FORMAT_PRETTY) {
    var jsonString = JSON.stringify(object, null, 2);
  } else if (options.format == FORMAT_MULTILINE) {
    var jsonString = Utilities.jsonStringify(object);
    jsonString = jsonString.replace(/},/gi, '},\n');
    jsonString = prettyJSON.replace(/":\[{"/gi, '":\n[{"');
    jsonString = prettyJSON.replace(/}\],/gi, '}],\n');
  } else {
    var jsonString = Utilities.jsonStringify(object);
  }
  if (options.language == LANGUAGE_PYTHON) {
    // add unicode markers
    jsonString = jsonString.replace(/"([a-zA-Z]*)":\s+"/gi, '"$1": u"');
  }
  return jsonString;
}

function displayText_(text) {
  var app = UiApp.createApplication().setTitle('Exported JSON');
  app.add(makeTextBox(app, 'json'));
  app.getElementById('json').setText(text);
  var ss = SpreadsheetApp.getActiveSpreadsheet(); 
  ss.show(app);
  return app; 
}

// getRowsData iterates row by row in the input range and returns an array of objects.
// Each object contains all the data for a given row, indexed by its normalized column name.
// Arguments:
//   - sheet: the sheet object that contains the data to be processed
// Returns an Array of objects.
function getRowsData_(sheet, options) {
  Logger.log("We're inside getRowsData_");
  var headersRange = sheet.getRange(1, 1, sheet.getFrozenRows(), sheet.getMaxColumns());
  var headers = headersRange.getValues()[0];
  var dataRange = sheet.getRange(sheet.getFrozenRows()+1, 1, sheet.getMaxRows(), sheet.getMaxColumns());
  var objects = getObjects_(dataRange.getValues(), normalizeHeaders_(headers));
  return objects;
}

// Makes a single flat object of key-value pairs, where the keys are in the first column,
// and corresponding values are in the second column.
function getRowsOfKVPs_(sheet) {
  Logger.log("We're inside getRowsOfKVPs_");
  var dataRange = sheet.getRange(sheet.getFrozenRows()+1, 1, sheet.getMaxRows(), 2);
  var data = dataRange.getValues();
  var bigFlatObject = {};
  for (var row = 0; row < data.length; ++row) {
    var keyCellData = data[row][0];
    if (isCellEmpty_(keyCellData)) {
      continue;
    }
    bigFlatObject[keyCellData] = data[row][1];
    Logger.log("keyCell: " + keyCellData + "; value: " + bigFlatObject[keyCellData]);
  }
  return bigFlatObject;
}

// Parse the decay config sheet
function getDecayData_(sheet) {
  Logger.log("We're inside getDecayData_");
  var dataRange = sheet.getRange(2, 1, sheet.getMaxRows(), 4);
  var data = dataRange.getValues();
  var destObj = {};
  destObj["DecayRates"] = {};
  destObj["DecayModifiers"] = {};
  var parsingRates = true; // otherwise, parsing modifiers
  var lastKeyword = "";
  var lastThreshold = -1;
  for (var row = 0; row < data.length; ++row) {
    var keyCellData = data[row][0];
    var col1Data = data[row][1];
    if (isCellEmpty_(keyCellData) && isCellEmpty_(col1Data)) {
      continue;
    }
    if (keyCellData == 'DECAY RATES:') {
      parsingRates = true;
      continue;
    }
    if (keyCellData == 'DECAY MODIFIERS:') {
      parsingRates = false;
      continue;
    }
    var curKeyword = lastKeyword;
    if (!isCellEmpty_(keyCellData)) {
      curKeyword = keyCellData;
    }
    lastKeyword = curKeyword;
    var col2Data = data[row][2];
    if (parsingRates) {
      // Parse the rates columns
      var rateConfig = {};
      rateConfig["Threshold"] = col1Data;
      rateConfig["DecayPerMinute"] = col2Data;
      if (destObj["DecayRates"][curKeyword] === undefined) {
        destObj["DecayRates"][curKeyword] = [];
      }
      destObj["DecayRates"][curKeyword].push(rateConfig);
    } else {
      // Parse the modifiers columns
      var col3Data = data[row][3];
      if (destObj["DecayModifiers"][curKeyword] === undefined) {
        destObj["DecayModifiers"][curKeyword] = [];
      }
      var curThreshold = col1Data;
      if (curThreshold != lastThreshold) {
        var thresholdObj = {};
        thresholdObj["Threshold"] = curThreshold;
        thresholdObj["OtherNeedsAffected"] = [];
        destObj["DecayModifiers"][curKeyword].push(thresholdObj);
      }
      var modifierConfig = {};
      modifierConfig["OtherNeedID"] = col2Data;
      modifierConfig["Multiplier"] = col3Data;
      var size = destObj["DecayModifiers"][curKeyword].length;
      destObj["DecayModifiers"][curKeyword][size - 1]["OtherNeedsAffected"].push(modifierConfig);
      lastThreshold = curThreshold;
    }
  }
  return destObj;
}

// Parse the rewards config sheet
function getRewardsData_(sheet) {
  Logger.log("We're inside getRewardsData_");
  var maxColumn = 120;
  var dataRange = sheet.getRange(4, 1, sheet.getMaxRows(), maxColumn);
  var data = dataRange.getValues();
  var levels = [];
  for (var row = 0; row < data.length; ++row) {
    var col0Data = data[row][0];
    var col1Data = data[row][1];
    var col2Data = data[row][2];
    if (isCellEmpty_(col0Data) && isCellEmpty_(col1Data) && isCellEmpty_(col2Data)) {
      break;  // First blank 'line' indicates end of table
    }
    var object = {};
    object["freeplayTargetSparksTotal"] = col1Data;
    object["freeplayMinSparksRewardPct"] = col2Data;
    object["freeplayMinSparksPct"] = data[row][3];
    object["freeplayMaxSparksPct"] = data[row][4];
    object["freeplayMinSparks"] = data[row][5];
    object["freeplayMinMaxSparks"] = data[row][6];    
    object["numStarsToUnlock"] = data[row][7];
    object["targetSparksTotal"] = data[row][8];
    object["minSparksPct"] = data[row][9];
    object["maxSparksPct"] = data[row][10];
    object["minSparks"] = data[row][11];
    object["minMaxSparks"] = data[row][12];
    object["maxPriorLevelUnlocks"] = data[row][13];
    var rewards = [];
    for (var col = 14; col <= maxColumn; col += 2) {
      var rewardTypeData = data[row][col];
      var rewardData = data[row][col + 1];
      if (isCellEmpty_(rewardTypeData)) {
        break;
      }
      var rewardObject = {};
      rewardObject["rewardType"] = rewardTypeData;
      rewardObject["data"] = rewardData;
      rewards.push(rewardObject);
    }
    object["rewards"] = rewards;
    levels.push(object);
  }
  var entireObject = {};
  entireObject["unlockLevels"] = levels;
  return entireObject;
}


// Parse the local notification config sheet
function getLocalNotificationData_(sheet) {
  Logger.log("We're inside getLocalNotificationData_");
  var maxColumn = 120;
  var firstDataRow = 3;
  var dataRange = sheet.getRange(firstDataRow, 1, sheet.getMaxRows(), maxColumn);
  var data = dataRange.getValues();
  var items = [];
  for (var row = 0; row < data.length; ++row) {
    var col0Data = data[row][0];
    var col1Data = data[row][1];
    var col2Data = data[row][2];
    var col3Data = data[row][3];
    var col4Data = data[row][4];
    var col5Data = data[row][5];
    var rowIsNotMainItem = isCellEmpty_(col0Data) && isCellEmpty_(col1Data) &&
                           isCellEmpty_(col2Data) && isCellEmpty_(col3Data) &&
                           isCellEmpty_(col4Data); 
    if (rowIsNotMainItem && isCellEmpty_(col5Data)) {
      break;  // First blank 'line' indicates end of table
    }
    if (rowIsNotMainItem) {
      // Pull in an alternate string key and add it to the last item
      if (items.length == 0) {        
        return("Error: First row of data needs to have notification type");
      }
      var object = items[items.length - 1];
      object["textKeys"].push(col5Data);
    } else {
      var col6Data = data[row][6];
      var col7Data = data[row][7];
      var col8Data = data[row][8];
      var col9Data = data[row][9];
      var col10Data = data[row][10];
      var col11Data = data[row][11];
      var col12Data = data[row][12];
      // This is a new item; parse everything including the first string key
      var object = {};
      var active = col0Data;
      //object["notificationType"] = col1Data;
      //object["param1"] = col2Data;
      //object["param2"] = col3Data;
      object["connection"] = col4Data;
      object["textKeys"] = [];
      object["textKeys"].push(col5Data);
      object["whenType"] = col6Data;    
      object["whenParam"]   = ParseTimeField(col7Data, firstDataRow + row, 7);
      object["rangeEarly"]  = ParseTimeField(col8Data, firstDataRow + row, 8);
      object["rangeLate"]   = ParseTimeField(col9Data, firstDataRow + row, 9);
      object["minimumDuration"] = ParseTimeField(col10Data, firstDataRow + row, 10);
      object["noEarlierThan"] = ParseTimeField(col11Data, firstDataRow + row, 11);
      object["noLaterThan"] = ParseTimeField(col12Data, firstDataRow + row, 12);
      // Error checking for non-type-specific fields:
      if (isCellEmpty_(col0Data) ||  // Note that this cell becomes a Boolean, not a string
          typeof(col0Data) !== "boolean") {
        return "Error in row " + (firstDataRow + row) + ": Active must be TRUE or FALSE";
      }
      if (col1Data != "General" &&
          col1Data != "NeedLevel" &&
          col1Data != "NeedBracket" &&
          col1Data != "DailyTokensToGo") {
        return "Error in row " + (firstDataRow + row) + ": NotificationType must be General, NeedLevel, NeedBracket or DailyTokensToGo";
      }
      if (col4Data != "Either" &&
          col4Data != "DidConnect" &&
          col4Data != "DidNotConnect") {
        return "Error in row " + (firstDataRow + row) + ": Connection must be DidConnect, DidNotConnect or Either";
      }
      if (col6Data != "NotApplicable" &&
          col6Data != "AfterAppOpen" &&
          col6Data != "AfterAppClose" &&
          col6Data != "ClockTime") {
        return "Error in row " + (firstDataRow + row) + ": WhenType must be AfterAppOpen, AfterAppClose, ClockTime or NotApplicable";
      }
      if (object["noEarlierThan"] > object["noLaterThan"]) {
        return "Error in row " + (firstDataRow + row) + ": NoEarlierThan must be a value less than NoLaterThan";
      }
      // Error checking for type-specific fields, AND package up the "UNION" fields
      var unionObject = {};
      switch (col1Data) {
        case "General":
          if (!isCellEmpty_(col2Data)) {
            return "Error in row " + (firstDataRow + row) + ": For General notification type, Param1 must be blank";
          }
          if (!isCellEmpty_(col3Data)) {
            return "Error in row " + (firstDataRow + row) + ": For General notification type, Param2 must be blank";
          }
          if (col6Data == "NotApplicable") {
            return "Error in row " + (firstDataRow + row) + ": For General notification type, WhenType cannot be NotApplicable";
          }
          unionObject["type"] = "notificationGeneral";
          break;
        case "NeedLevel":
          if (col2Data != "Repair" &&
              col2Data != "Energy" &&
              col2Data != "Play") {
            return "Error in row " + (firstDataRow + row) + ": For NeedLevel notification type, Param1 must be Repair, Energy or Play";
          }
          if (!isNumber(col3Data)) {
            return "Error in row " + (firstDataRow + row) + ": For NeedLevel notification type, Param2 must be a number";
          }
          if (col3Data < 0 || col3Data > 1) {
            return "Error in row " + (firstDataRow + row) + ": For NeedLevel notification type, Param2 must be a number in range 0 to 1";
          }
          if (col6Data != "NotApplicable") {
            return "Error in row " + (firstDataRow + row) + ": For NeedLevel notification type, WhenType must be NotApplicable";
          }
          unionObject["type"] = "notificationNeedLevel";
          unionObject["needId"] = col2Data;
          unionObject["level"] = col3Data;
          break;
        case "NeedBracket":
          if (col2Data != "Repair" &&
              col2Data != "Energy" &&
              col2Data != "Play") {
            return "Error in row " + (firstDataRow + row) + ": For NeedBracket notification type, Param1 must be Repair, Energy or Play";
          }
          if (col3Data != "Normal" &&
              col3Data != "Warning" &&
              col3Data != "Critical") {
            return "Error in row " + (firstDataRow + row) + ": For NeedLevel notification type, Param2 must be Normal, Warning or Critical";
          }
          if (col6Data != "NotApplicable") {
            return "Error in row " + (firstDataRow + row) + ": For NeedBracket notification type, WhenType must be NotApplicable";
          }
          unionObject["type"] = "notificationNeedBracket";
          unionObject["needId"] = col2Data;
          unionObject["needBracketId"] = col3Data;
          break;
        case "DailyTokensToGo":
          if (!isNormalInteger(col2Data)) {
            return "Error in row " + (firstDataRow + row) + ": For DailyTokensToGo notification type, Param1 must be a non-negative integer";
          }
          if (!isCellEmpty_(col3Data)) {
            return "Error in row " + (firstDataRow + row) + ": For DailyTokensToGo notification type, Param2 must be blank";
          }
          if (col6Data == "NotApplicable") {
            return "Error in row " + (firstDataRow + row) + ": For DailyTokensToGo notification type, WhenType cannot be NotApplicable";
          }
          unionObject["type"] = "notificationDailyTokensToGo";
          unionObject["numTokensToGo"] = col2Data;
          break;
      }
      object["notificationMainUnion"] = unionObject;
      if (active) {
        items.push(object);
      }
    }  // Endif !isRowMain
  } // End loop through rows
  var entireObject = {};
  entireObject["localNotificationConfigs"] = items;
  return entireObject;
}

function ParseTimeField(str, row, col) {
  if (str === "NotApplicable") {
    return -1;
  }
  // Parse 'clock time' format (HH:MM)
  str = String(str);
  var colonIndex = str.indexOf(":");
  if (colonIndex != -1) {
    var h = parseInt(str.substring(0, colonIndex));
    var m = parseInt(str.substring(colonIndex + 1));
    var totalMinutes = (h * 60) + m;
    if (totalMinutes < 0 || totalMinutes > ((24 * 60) - 1)) {
      return "Error in row " + row + ", col " + (col + 1) + ": Clock time must be in range 00:00 to 23:59";
    }
    return totalMinutes;
  }
  // Parse a number with suffix "s", "m", "h", "d", or "w" (default is "m")
  var len = str.length;
  var number = 0;
  if (len > 0) {
    number = parseFloat(str);
    var lastChar = str.charAt(len - 1);
    if (lastChar === 'w') {
      number = number * 60 * 24 * 7;
    }
    else if (lastChar === 'd') {
      number = number * 60 * 24;
    }
    else if (lastChar === 'h') {
      number = number * 60;
    }
    else if (lastChar === 's') {
      number = number / 60;
    }
    else if (lastChar !== 'm') {
      return "Error in row " + row + ", col " + (col + 1) + ": Invalid time duration suffix (must be s, m, h, d or w)";
    }
  }
  return number;
}


// getColumnsData iterates column by column in the input range and returns an array of objects.
// Each object contains all the data for a given column, indexed by its normalized row name.
// Arguments:
//   - sheet: the sheet object that contains the data to be processed
//   - range: the exact range of cells where the data is stored
//   - rowHeadersColumnIndex: specifies the column number where the row names are stored.
//       This argument is optional and it defaults to the column immediately left of the range; 
// Returns an Array of objects.
function getColumnsData_(sheet, range, rowHeadersColumnIndex) {
  rowHeadersColumnIndex = rowHeadersColumnIndex || range.getColumnIndex() - 1;
  var headersTmp = sheet.getRange(range.getRow(), rowHeadersColumnIndex, range.getNumRows(), 1).getValues();
  var headers = normalizeHeaders_(arrayTranspose_(headersTmp)[0]);
  return getObjects(arrayTranspose_(range.getValues()), headers);
}

function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function isNormalInteger(str) {
  return /^\+?(0|[1-9]\d*)$/.test(str);
}

// For every row of data in data, generates an object that contains the data. Names of
// object fields are defined in keys.
// Arguments:
//   - data: JavaScript 2d array
//   - keys: Array of Strings that define the property names for the objects to create
function getObjects_(data, keys) {
  var objects = [];
  for (var i = 0; i < data.length; ++i) {
    var object = {};
    var hasData = false;
    for (var j = 0; j < data[i].length; ++j) {
      var cellData = data[i][j];
      if (isCellEmpty_(cellData)) {
        continue;
      }
      object[keys[j]] = cellData;
      hasData = true;
    }
    if (hasData) {
      objects.push(object);
    }
  }
  return objects;
}

// Returns an Array of normalized Strings.
// Arguments:
//   - headers: Array of Strings to normalize
function normalizeHeaders_(headers) {
  var keys = [];
  for (var i = 0; i < headers.length; ++i) {
    var key = normalizeHeader_(headers[i]);
    if (key.length > 0) {
      keys.push(key);
    }
  }
  return keys;
}

// Normalizes a string, by removing all alphanumeric characters and using mixed case
// to separate words. The output will always start with a lower case letter.
// This function is designed to produce JavaScript object property names.
// Arguments:
//   - header: string to normalize
// Examples:
//   "First Name" -> "firstName"
//   "Market Cap (millions) -> "marketCapMillions
//   "1 number at the beginning is ignored" -> "numberAtTheBeginningIsIgnored"
function normalizeHeader_(header) {
  var key = "";
  var upperCase = false;
  for (var i = 0; i < header.length; ++i) {
    var letter = header[i];
    if (letter == " " && key.length > 0) {
      upperCase = true;
      continue;
    }
    if (!isAlnum_(letter)) {
      continue;
    }
    if (key.length == 0 && isDigit_(letter)) {
      continue; // first character must be a letter
    }
    if (upperCase) {
      upperCase = false;
      key += letter.toUpperCase();
    } else {
      key += letter.toLowerCase();
    }
  }
  return key;
}

// Returns true if the cell where cellData was read from is empty.
// Arguments:
//   - cellData: string
function isCellEmpty_(cellData) {
  return typeof(cellData) == "string" && cellData == "";
}

// Returns true if the character char is alphabetical, false otherwise.
function isAlnum_(char) {
  return char >= 'A' && char <= 'Z' ||
    char >= 'a' && char <= 'z' ||
    isDigit_(char);
}

// Returns true if the character char is a digit, false otherwise.
function isDigit_(char) {
  return char >= '0' && char <= '9';
}

// Given a JavaScript 2d Array, this function returns the transposed table.
// Arguments:
//   - data: JavaScript 2d Array
// Returns a JavaScript 2d Array
// Example: arrayTranspose([[1,2,3],[4,5,6]]) returns [[1,4],[2,5],[3,6]].
function arrayTranspose_(data) {
  if (data.length == 0 || data[0].length == 0) {
    return null;
  }

  var ret = [];
  for (var i = 0; i < data[0].length; ++i) {
    ret.push([]);
  }

  for (var i = 0; i < data.length; ++i) {
    for (var j = 0; j < data[i].length; ++j) {
      ret[j][i] = data[i][j];
    }
  }

  return ret;
}