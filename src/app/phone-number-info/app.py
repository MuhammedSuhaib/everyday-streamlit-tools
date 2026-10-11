import streamlit as st
# Top-level module for parse, validation, formatting, and enums
import phonenumbers
# Submodules required for metadata lookup (not automatically imported by phonenumbers)
from phonenumbers import carrier, geocoder, timezone
from src.components import render_header, render_footer

render_header("Phone Number Info")
st.markdown("Phone number tracker - Get location, carrier, and timezone information.")

phone_input = st.text_input(
    "Enter phone number",
    placeholder="+6281xxxxxxxxx",
    help="Include country code (e.g., +62 for Indonesia, +1 for US)",
)

if st.button("Track", type="primary"):
    if not phone_input:
        st.warning("Please enter a phone number")
    else:
        try:
            parsed = phonenumbers.parse(phone_input, None)

            if not phonenumbers.is_possible_number(parsed):
                st.error("This number is not possible")
            elif not phonenumbers.is_valid_number(parsed):
                st.warning("This number may not be valid")
            else:
                region_code = phonenumbers.region_code_for_number(parsed)
                provider = carrier.name_for_number(parsed, "en")
                location = geocoder.description_for_number(parsed, "en")
                intl_format = phonenumbers.format_number(
                    parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )
                mobile_format = phonenumbers.format_number_for_mobile_dialing(
                    parsed, region_code, with_formatting=True
                )
                number_type = phonenumbers.number_type(parsed)
                tz_list = timezone.time_zones_for_number(parsed)

                st.success("✅ Valid phone number")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("🌍 Location", location or "Unknown")
                    st.metric("🏷️ Region Code", region_code)
                    st.metric("📡 Carrier", provider or "Unknown")
                    st.metric("⏰ Timezone", ", ".join(tz_list) if tz_list else "Unknown")

                with col2:
                    st.metric("📞 International", intl_format)
                    st.metric("📱 Mobile Format", mobile_format)
                    st.metric("🔢 Country Code", parsed.country_code)
                    st.metric("🔢 Local Number", parsed.national_number)

                type_map = {
                    phonenumbers.PhoneNumberType.MOBILE: "Mobile",
                    phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed-line",
                    phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed-line or Mobile",
                    phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-free",
                    phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium-rate",
                    phonenumbers.PhoneNumberType.SHARED_COST: "Shared-cost",
                    phonenumbers.PhoneNumberType.VOIP: "VoIP",
                    phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal",
                    phonenumbers.PhoneNumberType.PAGER: "Pager",
                    phonenumbers.PhoneNumberType.UAN: "UAN",
                    phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
                    phonenumbers.PhoneNumberType.UNKNOWN: "Unknown",
                }
                st.info(f"**Type:** {type_map.get(number_type, 'Unknown')}")

        except phonenumbers.NumberParseException as e:
            st.error(f"Invalid format: {e}")
        except Exception as e:
            st.error(f"Error: {e}")

render_footer("Phone Number Info")
