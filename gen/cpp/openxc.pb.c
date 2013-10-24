/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.2.4-dev at Wed Oct 23 08:59:20 2013. */

#include "openxc.pb.h"



const pb_field_t openxc_VehicleMessage_fields[9] = {
    PB_FIELD2(  1, ENUM    , OPTIONAL, STATIC, FIRST, openxc_VehicleMessage, type, type, 0),
    PB_FIELD2(  2, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, raw_message, type, &openxc_RawMessage_fields),
    PB_FIELD2(  3, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, string_message, raw_message, &openxc_StringMessage_fields),
    PB_FIELD2(  4, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, numeric_message, string_message, &openxc_NumericMessage_fields),
    PB_FIELD2(  5, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, boolean_message, numeric_message, &openxc_BooleanMessage_fields),
    PB_FIELD2(  6, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, evented_string_message, boolean_message, &openxc_EventedStringMessage_fields),
    PB_FIELD2(  7, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, evented_boolean_message, evented_string_message, &openxc_EventedBooleanMessage_fields),
    PB_FIELD2(  8, MESSAGE , OPTIONAL, STATIC, OTHER, openxc_VehicleMessage, evented_numeric_message, evented_boolean_message, &openxc_EventedNumericMessage_fields),
    PB_LAST_FIELD
};

const pb_field_t openxc_RawMessage_fields[3] = {
    PB_FIELD2(  1, INT32   , OPTIONAL, STATIC, FIRST, openxc_RawMessage, bus, bus, 0),
    PB_FIELD2(  2, UINT32  , OPTIONAL, STATIC, OTHER, openxc_RawMessage, message_id, bus, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_StringMessage_fields[3] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_StringMessage, name, name, 0),
    PB_FIELD2(  2, STRING  , OPTIONAL, STATIC, OTHER, openxc_StringMessage, value, name, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_NumericMessage_fields[3] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_NumericMessage, name, name, 0),
    PB_FIELD2(  2, DOUBLE  , OPTIONAL, STATIC, OTHER, openxc_NumericMessage, value, name, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_BooleanMessage_fields[3] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_BooleanMessage, name, name, 0),
    PB_FIELD2(  2, BOOL    , OPTIONAL, STATIC, OTHER, openxc_BooleanMessage, value, name, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_EventedStringMessage_fields[4] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_EventedStringMessage, name, name, 0),
    PB_FIELD2(  2, STRING  , OPTIONAL, STATIC, OTHER, openxc_EventedStringMessage, value, name, 0),
    PB_FIELD2(  3, STRING  , OPTIONAL, STATIC, OTHER, openxc_EventedStringMessage, event, value, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_EventedBooleanMessage_fields[4] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_EventedBooleanMessage, name, name, 0),
    PB_FIELD2(  2, STRING  , OPTIONAL, STATIC, OTHER, openxc_EventedBooleanMessage, value, name, 0),
    PB_FIELD2(  3, BOOL    , OPTIONAL, STATIC, OTHER, openxc_EventedBooleanMessage, event, value, 0),
    PB_LAST_FIELD
};

const pb_field_t openxc_EventedNumericMessage_fields[4] = {
    PB_FIELD2(  1, STRING  , OPTIONAL, STATIC, FIRST, openxc_EventedNumericMessage, name, name, 0),
    PB_FIELD2(  2, STRING  , OPTIONAL, STATIC, OTHER, openxc_EventedNumericMessage, value, name, 0),
    PB_FIELD2(  3, DOUBLE  , OPTIONAL, STATIC, OTHER, openxc_EventedNumericMessage, event, value, 0),
    PB_LAST_FIELD
};


/* Check that field information fits in pb_field_t */
#if !defined(PB_FIELD_16BIT) && !defined(PB_FIELD_32BIT)
STATIC_ASSERT((pb_membersize(openxc_VehicleMessage, raw_message) < 256 && pb_membersize(openxc_VehicleMessage, string_message) < 256 && pb_membersize(openxc_VehicleMessage, numeric_message) < 256 && pb_membersize(openxc_VehicleMessage, boolean_message) < 256 && pb_membersize(openxc_VehicleMessage, evented_string_message) < 256 && pb_membersize(openxc_VehicleMessage, evented_boolean_message) < 256 && pb_membersize(openxc_VehicleMessage, evented_numeric_message) < 256), YOU_MUST_DEFINE_PB_FIELD_16BIT_FOR_MESSAGES_openxc_VehicleMessage_openxc_RawMessage_openxc_StringMessage_openxc_NumericMessage_openxc_BooleanMessage_openxc_EventedStringMessage_openxc_EventedBooleanMessage_openxc_EventedNumericMessage)
#endif

#if !defined(PB_FIELD_32BIT)
STATIC_ASSERT((pb_membersize(openxc_VehicleMessage, raw_message) < 65536 && pb_membersize(openxc_VehicleMessage, string_message) < 65536 && pb_membersize(openxc_VehicleMessage, numeric_message) < 65536 && pb_membersize(openxc_VehicleMessage, boolean_message) < 65536 && pb_membersize(openxc_VehicleMessage, evented_string_message) < 65536 && pb_membersize(openxc_VehicleMessage, evented_boolean_message) < 65536 && pb_membersize(openxc_VehicleMessage, evented_numeric_message) < 65536), YOU_MUST_DEFINE_PB_FIELD_32BIT_FOR_MESSAGES_openxc_VehicleMessage_openxc_RawMessage_openxc_StringMessage_openxc_NumericMessage_openxc_BooleanMessage_openxc_EventedStringMessage_openxc_EventedBooleanMessage_openxc_EventedNumericMessage)
#endif

/* On some platforms (such as AVR), double is really float.
 * These are not directly supported by nanopb, but see example_avr_double.
 * To get rid of this error, remove any double fields from your .proto.
 */
STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)

