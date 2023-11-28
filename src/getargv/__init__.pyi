# encoding info: https://docs.python.org/3/library/codecs.html#standard-encodings
from typing import Literal
ASCII = Literal["ascii", "646", "us-ascii"]
BIG5 = Literal["big5", "big5-tw", "csbig5"]
BIG5HKSCS = Literal["big5hkscs", "big5-hkscs", "hkscs"]
CP037 = Literal["cp037", "IBM037", "IBM039"]
CP273 = Literal["cp273", "273", "IBM273", "csIBM273"]
CP424 = Literal["cp424", "EBCDIC-CP-HE", "IBM424"]
CP437 = Literal["cp437", "437", "IBM437"]
CP500 = Literal["cp500", "EBCDIC-CP-BE", "EBCDIC-CP-CH", "IBM500"]
CP720 = Literal["cp720"]
CP737 = Literal["cp737"]
CP775 = Literal["cp775", "IBM775"]
CP850 = Literal["cp850", "850", "IBM850"]
CP852 = Literal["cp852", "852", "IBM852"]
CP855 = Literal["cp855", "855", "IBM855"]
CP856 = Literal["cp856"]
CP857 = Literal["cp857", "857", "IBM857"]
CP858 = Literal["cp858", "858", "IBM858"]
CP860 = Literal["cp860", "860", "IBM860"]
CP861 = Literal["cp861", "861", "CP-IS", "IBM861"]
CP862 = Literal["cp862", "862", "IBM862"]
CP863 = Literal["cp863", "863", "IBM863"]
CP864 = Literal["cp864", "IBM864"]
CP865 = Literal["cp865", "865", "IBM865"]
CP866 = Literal["cp866", "866", "IBM866"]
CP869 = Literal["cp869", "869", "CP-GR", "IBM869"]
CP874 = Literal["cp874"]
CP875 = Literal["cp875"]
CP932 = Literal["cp932", "932", "ms932", "mskanji", "ms-kanji"]
CP949 = Literal["cp949", "949", "ms949", "uhc"]
CP950 = Literal["cp950", "950", "ms950"]
CP1006 = Literal["cp1006"]
CP1026 = Literal["cp1026", "ibm1026"]
CP1125 = Literal["cp1125", "1125", "ibm1125", "cp866u", "ruscii"]
CP1140 = Literal["cp1140", "ibm1140"]
CP1250 = Literal["cp1250", "windows-1250"]
CP1251 = Literal["cp1251", "windows-1251"]
CP1252 = Literal["cp1252", "windows-1252"]
CP1253 = Literal["cp1253", "windows-1253"]
CP1254 = Literal["cp1254", "windows-1254"]
CP1255 = Literal["cp1255", "windows-1255"]
CP1256 = Literal["cp1256", "windows-1256"]
CP1257 = Literal["cp1257", "windows-1257"]
CP1258 = Literal["cp1258", "windows-1258"]
EUC_JP = Literal["euc_jp", "eucjp", "ujis", "u-jis"]
EUC_JIS_2004 = Literal["euc_jis_2004", "jisx0213", "eucjis2004"]
EUC_JISX0213 = Literal["euc_jisx0213", "eucjisx0213"]
EUC_KR = Literal["euc_kr", "euckr", "korean", "ksc5601", "ks_c-5601", "ks_c-5601-1987", "ksx1001", "ks_x-1001"]
GB2312 = Literal["gb2312", "chinese", "csiso58gb231280", "euc-cn", "euccn", "eucgb2312-cn", "gb2312-1980", "gb2312-80", "iso-ir-58"]
GBK = Literal["gbk", "936", "cp936", "ms936"]
GB18030 = Literal["gb18030", "gb18030-2000"]
HZ = Literal["hz", "hzgb", "hz-gb", "hz-gb-2312"]
ISO2022_JP = Literal["iso2022_jp", "csiso2022jp", "iso2022jp", "iso-2022-jp"]
ISO2022_JP_1 = Literal["iso2022_jp_1", "iso2022jp-1", "iso-2022-jp-1"]
ISO2022_JP_2 = Literal["iso2022_jp_2", "iso2022jp-2", "iso-2022-jp-2"]
ISO2022_JP_2004 = Literal["iso2022_jp_2004", "iso2022jp-2004", "iso-2022-jp-2004"]
ISO2022_JP_3 = Literal["iso2022_jp_3", "iso2022jp-3", "iso-2022-jp-3"]
ISO2022_JP_EXT = Literal["iso2022_jp_ext", "iso2022jp-ext", "iso-2022-jp-ext"]
ISO2022_KR = Literal["iso2022_kr", "csiso2022kr", "iso2022kr", "iso-2022-kr"]
LATIN_1 = Literal["latin_1", "iso-8859-1", "iso8859-1", "8859", "cp819", "latin", "latin1", "L1"]
ISO8859_2 = Literal["iso8859_2", "iso-8859-2", "latin2", "L2"]
ISO8859_3 = Literal["iso8859_3", "iso-8859-3", "latin3", "L3"]
ISO8859_4 = Literal["iso8859_4", "iso-8859-4", "latin4", "L4"]
ISO8859_5 = Literal["iso8859_5", "iso-8859-5", "cyrillic"]
ISO8859_6 = Literal["iso8859_6", "iso-8859-6", "arabic"]
ISO8859_7 = Literal["iso8859_7", "iso-8859-7", "greek", "greek8"]
ISO8859_8 = Literal["iso8859_8", "iso-8859-8", "hebrew"]
ISO8859_9 = Literal["iso8859_9", "iso-8859-9", "latin5", "L5"]
ISO8859_10 = Literal["iso8859_10", "iso-8859-10", "latin6", "L6"]
ISO8859_11 = Literal["iso8859_11", "iso-8859-11", "thai"]
ISO8859_13 = Literal["iso8859_13", "iso-8859-13", "latin7", "L7"]
ISO8859_14 = Literal["iso8859_14", "iso-8859-14", "latin8", "L8"]
ISO8859_15 = Literal["iso8859_15", "iso-8859-15", "latin9", "L9"]
ISO8859_16 = Literal["iso8859_16", "iso-8859-16", "latin10", "L10"]
JOHAB = Literal["johab", "cp1361", "ms1361"]
KOI8_R = Literal["koi8_r"]
KOI8_T = Literal["koi8_t"]
KOI8_U = Literal["koi8_u"]
KZ1048 = Literal["kz1048", "kz_1048", "strk1048_2002", "rk1048"]
MAC_CYRILLIC = Literal["mac_cyrillic", "maccyrillic"]
MAC_GREEK = Literal["mac_greek", "macgreek"]
MAC_ICELAND = Literal["mac_iceland", "maciceland"]
MAC_LATIN2 = Literal["mac_latin2", "maclatin2", "maccentraleurope", "mac_centeuro"]
MAC_ROMAN = Literal["mac_roman", "macroman", "macintosh"]
MAC_TURKISH = Literal["mac_turkish", "macturkish"]
PTCP154 = Literal["ptcp154", "csptcp154", "pt154", "cp154", "cyrillic-asian"]
SHIFT_JIS = Literal["shift_jis", "csshiftjis", "shiftjis", "sjis", "s_jis"]
SHIFT_JIS_2004 = Literal["shift_jis_2004", "shiftjis2004", "sjis_2004", "sjis2004"]
SHIFT_JISX0213 = Literal["shift_jisx0213", "shiftjisx0213", "sjisx0213", "s_jisx0213"]
UTF_32 = Literal["utf_32", "U32", "utf32"]
UTF_32_BE = Literal["utf_32_be", "UTF-32BE"]
UTF_32_LE = Literal["utf_32_le", "UTF-32LE"]
UTF_16 = Literal["utf_16", "U16", "utf16"]
UTF_16_BE = Literal["utf_16_be", "UTF-16BE"]
UTF_16_LE = Literal["utf_16_le", "UTF-16LE"]
UTF_7 = Literal["utf_7", "U7", "unicode-1-1-utf-7"]
UTF_8 = Literal["utf_8", "U8", "UTF", "utf8", "cp65001"]
UTF_8_SIG = Literal["utf_8_sig"]

Encodings = Literal[ASCII, BIG5, BIG5HKSCS, CP037, CP273, CP424, CP437, CP500, CP720, CP737, CP775, CP850, CP852, CP855, CP856, CP857, CP858, CP860, CP861, CP862, CP863, CP864, CP865, CP866, CP869, CP874, CP875, CP932, CP949, CP950, CP1006, CP1026, CP1125, CP1140, CP1250, CP1251, CP1252, CP1253, CP1254, CP1255, CP1256, CP1257, CP1258, EUC_JP, EUC_JIS_2004, EUC_JISX0213, EUC_KR, GB2312, GBK, GB18030, HZ, ISO2022_JP, ISO2022_JP_1, ISO2022_JP_2, ISO2022_JP_2004, ISO2022_JP_3, ISO2022_JP_EXT, ISO2022_KR, LATIN_1, ISO8859_2, ISO8859_3, ISO8859_4, ISO8859_5, ISO8859_6, ISO8859_7, ISO8859_8, ISO8859_9, ISO8859_10, ISO8859_11, ISO8859_13, ISO8859_14, ISO8859_15, ISO8859_16, JOHAB, KOI8_R, KOI8_T, KOI8_U, KZ1048, MAC_CYRILLIC, MAC_GREEK, MAC_ICELAND, MAC_LATIN2, MAC_ROMAN, MAC_TURKISH, PTCP154, SHIFT_JIS, SHIFT_JIS_2004, SHIFT_JISX0213, UTF_32, UTF_32_BE, UTF_32_LE, UTF_16, UTF_16_BE, UTF_16_LE, UTF_7, UTF_8, UTF_8_SIG]

__version__: str
from _getargv import *

def as_string(pid: int, encoding: Encodings, skip: int = 0, nuls: bool = False) -> str: ...
def as_string_list(pid: int, encoding: Encodings) -> list[str]: ...
def as_bytes(pid: int, skip: int = 0, nuls: bool = False) -> bytes: ...
def as_list(pid: int) -> list[bytes]: ...