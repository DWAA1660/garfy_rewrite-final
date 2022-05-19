from nextcord.ext import commands
from nextcord import Interaction
from nextcord import slash_command
import nextcord
import copy


def PixelPainter_prep_board(board):
  b = ""
  for x in board:
    b += "".join(x) + "\n"

  return b + "."


class PixelPainter(nextcord.ui.View):
  def __init__(self, board, x, y, author):
    super().__init__()
    self.value = board
    self.xy = [0, 0]
    self.xs = x
    self.ys = y
    self.msg = None
    self.author = author

  @nextcord.ui.button(label=" ", style=nextcord.ButtonStyle.gray, row=0)
  async def blank1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Up", style=nextcord.ButtonStyle.blurple, row=0)
  async def Up(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      if self.xy[0] > 0:
        self.xy[0] -= 1
        self.x = copy.deepcopy(self.value)
        self.x[self.xy[0]][self.xy[1]] = "XX"
        await self.msg.edit(PixelPainter_prep_board(self.x))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label=" ", style=nextcord.ButtonStyle.gray, row=0)
  async def blank2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Left", style=nextcord.ButtonStyle.blurple, row=1)
  async def Left(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      if self.xy[1] > 0:
        self.xy[1] -= 1
        self.x = copy.deepcopy(self.value)
        self.x[self.xy[0]][self.xy[1]] = "XX"
        await self.msg.edit(PixelPainter_prep_board(self.x))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="Down", style=nextcord.ButtonStyle.blurple, row=1)
  async def Down(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      if self.xy[0] < self.ys - 1:
        self.xy[0] += 1
        self.x = copy.deepcopy(self.value)
        self.x[self.xy[0]][self.xy[1]] = "XX"
        await self.msg.edit(PixelPainter_prep_board(self.x))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="Right", style=nextcord.ButtonStyle.blurple, row=1)
  async def Right(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      if self.xy[1] < self.xs - 1:
        self.xy[1] += 1
        self.x = copy.deepcopy(self.value)
        self.x[self.xy[0]][self.xy[1]] = "XX"
        await self.msg.edit(PixelPainter_prep_board(self.x))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="Paint", style=nextcord.ButtonStyle.green, row=2)
  async def Paint(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      v = self.value[self.xy[0]][self.xy[1]]

      if v == "⬜":
        self.value[self.xy[0]][self.xy[1]] = "⬛"
      else:
        self.value[self.xy[0]][self.xy[1]] = "⬜"

      await self.msg.edit(PixelPainter_prep_board(self.value))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="Settings", style=nextcord.ButtonStyle.gray, row=2)
  async def settings(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      newview = PixelPainterSettings(self.msg, self.value, self.xs, self.ys, self.xy, self.author)
      await self.msg.edit(PixelPainter_prep_board(self.value), view=newview)
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="Done", style=nextcord.ButtonStyle.red, row=2)
  async def Done(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      await self.msg.edit(PixelPainter_prep_board(self.value)[:-1], view=None)
      self.stop()
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)


class PixelPainterSettings(nextcord.ui.View):
  def __init__(self, msg, board, x, y, xy, author):
    super().__init__()
    self.value = None
    self.msg = msg
    self.board = board
    self.xs = x
    self.ys = y
    self.xy = xy
    self.author = author

  @nextcord.ui.button(label="Back", style=nextcord.ButtonStyle.blurple, row=0)
  async def Back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      newview = PixelPainter(self.board, self.xs, self.ys, self.author)
      newview.msg = self.msg
      newview.xy = self.xy
      await self.msg.edit(PixelPainter_prep_board(self.board), view=newview)
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label=" ", style=nextcord.ButtonStyle.gray, row=0)
  async def blank1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Delete", style=nextcord.ButtonStyle.red, row=0)
  async def Delete(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      await self.msg.delete()
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)

  @nextcord.ui.button(label="-----", style=nextcord.ButtonStyle.gray, row=1)
  async def blank2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Effects", style=nextcord.ButtonStyle.gray, row=1)
  async def blank3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="-----", style=nextcord.ButtonStyle.gray, row=1)
  async def blank4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    pass

  @nextcord.ui.button(label="Invert", style=nextcord.ButtonStyle.blurple, row=2)
  async def invert(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
    if interaction.user == self.author:
      for i in range(0, len(self.board)):
        for j in range(0, len(self.board[i])):
          if self.board[i][j] == "⬛":
            self.board[i][j] = "⬜"
          else:
            self.board[i][j] = "⬛"

      await self.msg.edit(PixelPainter_prep_board(self.board))
    else:
      await interaction.response.send_message("This isn't your button!", ephemeral=True)


class painter(commands.Cog):

  def __init__(self, client):
    self.client = client

  @slash_command()
  async def pixelpainter(self, ctx: Interaction, xsize=5, ysize=5):
    xsize = int(xsize)
    ysize = int(ysize)
    y = [x for x in "⬜" * xsize]
    board = [copy.deepcopy(y) for x in range(0, ysize)]
    view = PixelPainter(board, xsize, ysize, ctx.user)
    await ctx.send(PixelPainter_prep_board(board), view=view)

    msg = None
    async for message in ctx.channel.history(limit=1):
      msg = message

    view.msg = msg

    await view.wait()


def setup(client):
  client.add_cog(painter(client))
