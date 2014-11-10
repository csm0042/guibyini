__author__ = 'chris.maue'


class PlaceSettings(object):
    def __init__(self, anchor, bordermode, height, width, relHeight, relWidth, relX, relY, offsetX, offsetY):
        self.anchor = anchor
        self.bordermode = bordermode
        self.height = height
        self.width = width
        self.relHeight = relHeight
        self.relWidth = relWidth
        self.relX = relX
        self.relY = relY
        self.offsetX = offsetX
        self.offsetY = offsetY


class FrameWidget(object):
    def __init__(self, backgroundColor, borderwidth, colormap, container, cursor, height, highlightBackground,
                 highlightColor, highlightThickness, padX, padY, relief, takeFocus, visual, width):
        self.backgroundColor = backgroundColor
        self.borderwidth = borderwidth
        self.colormap = colormap
        self.container = container
        self.cursor = cursor
        self.height = height
        self.highlightBackground = highlightBackground
        self.highlightColor = highlightColor
        self.highlightThickness = highlightThickness
        self.padX = padX
        self.padY = padY
        self.relief = relief
        self.takeFocus = takeFocus
        self.visual = visual
        self.width = width


class MessageWidget(object):
    def __init__(self):
    #def __init__(self, anchor, aspect, backgroundColor, borderwidth, cursor, font, fontSize, foregroundColor,
    #             highlightBackground, highlightBackgroundColor, highlightThickness, justify, padX, padY, relief,
    #             takeFocus, text, textVariable, width):
        self.anchor = anchor
        self.aspect = aspect
        self.backgroundColor = backgroundColor
        self.borderwidth = borderwidth
        self.cursor = cursor
        self.font = font
        self.fontSize = fontSize
        self.foregroundColor = foregroundColor
        self.highlightBackground = highlightBackground
        self.highlightBackgroundColor = highlightBackgroundColor
        self.highlightThickness = highlightThickness
        self.justify = justify
        self.padX = padX
        self.padY = padY
        self.relief = relief
        self.takeFocus = takeFocus
        self.text = text
        self.textVariable = textVariable
        self.width = width


class TextWidget(object):
    def __init__(self):
    #def __init__(self, autoSeparators, backgroundColor, backgroundStipple, borderwidth, cursor, exportSelection, font,
    #             fontSize, foregroundColor, foregroundStipple, height, highlightBackground, highlightColor,
    #             highlightThickness, insertBackground, insertBorderwidth, insertOffTime, insertOnTime, insertWidth,
    #             justify, lmargin1, lmargin2, maxUndo, padX, padY, offset, overstrike, relief, rmargin,
    #             selectBackgroundColor, selectForegroundColor, selectBorderwidth, setGrid, spacing1, spacing2, spacing3,
    #             state, tabs, takeFocus, text, underline, undo, width, wrap, xScrollCommand, yScrollCommand):
        self.autoSeparators = autoSeparators
        self.backgroundColor = backgroundColor
        self.backgroundStipple = backgroundStipple
        self.borderwidth = borderwidth
        self.cursor = cursor
        self.exportSelection = exportSelection
        self.font = font
        self.fontSize = fontSize
        self.foregroundColor = foregroundColor
        self.foregroundStipple = foregroundStipple
        self.height = height
        self.highlightBackground = highlightBackground
        self.highlightColor = highlightColor
        self.highlightThickness = highlightThickness
        self.insertBackground = insertBackground
        self.insertBorderwidth = insertBorderwidth
        self.insertOffTime = insertOffTime
        self.insertOnTime = insertOnTime
        self.insertWidth = insertWidth
        self.justify = justify
        self.lmargin1 = lmargin1
        self.lmargin2 = lmargin2
        self.maxUndo = maxUndo
        self.padX = padX
        self.padY = padY
        self.offset = offset
        self.overstrike = overstrike
        self.relief = relief
        self.rmargin = rmargin
        self.selectBackgroundColor = selectBackgroundColor
        self.selectForegroundColor = selectForegroundColor
        self.selectBorderwidth = selectBorderwidth
        self.setGrid = setGrid
        self.spacing1 = spacing1
        self.spacing2 = spacing2
        self.spacing3 = spacing3
        self.state = state
        self.tabs = tabs
        self.takeFocus = takeFocus
        self.text = text
        self.underline = underline
        self.undo = undo
        self.width = width
        self.wrap = wrap
        self.xScrollCommand = xScrollCommand
        self.yScrollCommand = yScrollCommand


class ButtonWidget(object):
    def __init__(self):
    #def __init__(self, activeBackgroundColor, activeForegroundColor, anchor, backgroundColor, bitmap, borderwidth,
    #             command, compound, cursor, default, disabledForeground, font, fontSize, foregroundColor, height,
    #             highlightBackgroundColor, highlightColor, highlightThickness, image, justify, overRelief, padX,
    #             padY, relief, repeatDelay, repeatInterval, state, takeFocus, text, textVariable, underline, width,
    #             wrapLength):
        self.activeBackgroundColor = activeBackgroundColor
        self.activeForegroundColor = activeForegroundColor
        self.anchor = anchor
        self.backgroundColor = backgroundColor
        self.bitmap = bitmap
        self.borderwidth = borderwidth
        self.command = command
        self.compound = compound
        self.cursor = cursor
        self.default = default
        self.disabledForeground = disabledForeground
        self.font = font
        self.fontSize = fontSize
        self.foregroundColor = foregroundColor
        self.height = height
        self.highlightBackgroundColor = highlightBackgroundColor
        self.highlightColor = highlightColor
        self.highlightThickness = highlightThickness
        self.image = image
        self.justify = justify
        self.overRelief = overRelief
        self.padX = padX
        self.padY = padY
        self.relief = relief
        self.repeatDelay = repeatDelay
        self.repeatInterval = repeatInterval
        self.state = state
        self.takeFocus = takeFocus
        self.text = text
        self.textVariable = textVariable
        self.underline = underline
        self.width = width
        self.wrapLength = wrapLength