import streamlit as st
import model

# Simple Streamlit UI for a Translator Agent
# The UI **calls** a function named `run(source_lang, target_lang, source_sentence)`
# Provide that function (or import it) in the same Python session when running this app.

LANGUAGES = {
    "English": "English",
    "Arabic": "Arabic",
    "French": "French",
    "Spanish": "Spanish",
    "German": "German",
    "Chinese (Simplified)": "Chinese",
    "Russian": "Russian",
    "Portuguese": "Portuguese",
    "Italian": "Italian",
}


def translate_click():
    src_text = st.session_state.get("source_text", "").strip()
    if not src_text:
        st.warning("Please enter a source sentence to translate.")
        return

    src_lang_code = LANGUAGES[st.session_state.src_selected]
    tgt_lang_code = LANGUAGES[st.session_state.tgt_selected]

    with st.spinner("Translating..."):
        try:
            # Call the user-provided run(...) function. It should be available in the app's namespace.
            translator_agent=model.translator()
            result = translator_agent.run(src_lang_code, tgt_lang_code, src_text)
            print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            # store output in session state so the output text_area shows it
            st.session_state.output = result if result is not None else ""
        except NameError:
            st.error("`run` function is not defined. Define or import `run(source_lang, target_lang, source_sentence)` before running this app.")
        except Exception as e:
            st.error(f"Error while calling `run`: {e}")


def swap_click():
    # swap selected languages
    a = st.session_state.src_selected
    b = st.session_state.tgt_selected
    st.session_state.src_selected = b
    st.session_state.tgt_selected = a
    # swap texts too
    src = st.session_state.get("source_text", "")
    out = st.session_state.get("output", "")
    st.session_state.source_text = out
    st.session_state.output = src


def main():
    st.set_page_config(page_title="Translator Agent UI", layout="wide")
    st.title("Translator Agent")

    st.markdown(
        "Use the dropdowns to choose source and target languages, type or paste the source sentence, then press **Translate**.\n\n"
    )

    # initialize session state keys for language selection and textboxes
    if "src_selected" not in st.session_state:
        st.session_state.src_selected = list(LANGUAGES.keys())[0]
    if "tgt_selected" not in st.session_state:
        # pick a different default if available
        names = list(LANGUAGES.keys())
        st.session_state.tgt_selected = names[1] if len(names) > 1 else names[0]
    if "source_text" not in st.session_state:
        st.session_state.source_text = ""
    if "output" not in st.session_state:
        st.session_state.output = ""

    left, right = st.columns(2)

    with left:
        st.subheader("Source")
        st.selectbox("Source language", list(LANGUAGES.keys()), key="src_selected")
        st.text_area("Source sentence", key="source_text", height=240)

    with right:
        st.subheader("Target")
        st.selectbox("Target language", list(LANGUAGES.keys()), key="tgt_selected")
        # readonly output area
        st.text_area("Translated output", value=st.session_state.get("output", ""), height=240, key="output_area", disabled=True)

    c1, c2, _ = st.columns([1, 1, 6])
    with c1:
        st.button("Translate", on_click=translate_click)
    with c2:
        st.button("Swap languages/text", on_click=swap_click)

    st.markdown("---")


if __name__ == "__main__":
    main()
