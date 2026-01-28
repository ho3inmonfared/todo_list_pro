const defaultConfig = {
    list_title: 'کارهای امروز',
    background_color: '#f8fafc',
    primary_color: '#6366f1',
    text_color: '#374151'
};

let config = { ...defaultConfig };

async function onConfigChange(newConfig) {
    const titleEl = document.getElementById('list-title');
    if (titleEl) {
        titleEl.textContent = newConfig.list_title || defaultConfig.list_title;
    }
}

function mapToCapabilities(cfg) {
    return {
        recolorables: [
            {
                get: () => cfg.primary_color || defaultConfig.primary_color,
                set: (value) => {
                    cfg.primary_color = value;
                    if (window.elementSdk) {
                        window.elementSdk.setConfig({ primary_color: value });
                    }
                }
            }
        ],
        borderables: [],
        fontEditable: undefined,
        fontSizeable: undefined
    };
}

function mapToEditPanelValues(cfg) {
    return new Map([
        ['list_title', cfg.list_title || defaultConfig.list_title]
    ]);
}

if (window.elementSdk) {
    window.elementSdk.init({
        defaultConfig,
        onConfigChange,
        mapToCapabilities,
        mapToEditPanelValues
    });
}